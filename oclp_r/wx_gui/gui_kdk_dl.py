import wx
import locale
import logging
import threading
import requests
from pathlib import Path
from .. import (
    constants,
    sucatalog
)
from ..wx_gui import (
    gui_main_menu,
    gui_support,
    gui_download,
)
from ..support import (
    utilities,
    network_handler,
)
KDK_API_LINK_ORIGIN:str  = "https://pyquick.github.io/KdkSupportPkg/manifest.json"
KDK_API_LINK_PROXY:str  = "https://oclpapi.simplehac.cn/KdkSupportPkg/manifest.json"
class KDKDownloadFrame(wx.Frame):
    def __init__(self, parent: wx.Frame, title: str, global_constants: constants.Constants,screen_location: tuple = None):
        logging.info("Initializing KDK Download Frame")
        self.constants: constants.Constants = global_constants
        self.title: str = title
        self.parent: wx.Frame = parent
        icon_path = str(self.constants.icns_resource_path / "Package.icns")
        self.icons = [self._icon_to_bitmap(icon_path), self._icon_to_bitmap(icon_path, (64, 64))]
        self.repl=False
        self.path_validate=None
        self.retry_download:bool=False
        self.validate_ins=None
        self.available_installers = None
        self.available_installers_latest = None
        self.kdk_data = None
        self.show_fully=False
        self.kdk_data_full=None
        self.backup_item=None
        self.kdk_data_latest = None
        self.catalog_seed: sucatalog.SeedType = sucatalog.SeedType.DeveloperSeed
        self.frame_modal = wx.Dialog(parent, title=title, size=(330, 200))
        self.on_download()
    def _icon_to_bitmap(self, icon: str, size: tuple = (32, 32)) -> wx.Bitmap:
        return wx.Bitmap(wx.Bitmap(icon, wx.BITMAP_TYPE_ICON).ConvertToImage().Rescale(size[0], size[1], wx.IMAGE_QUALITY_HIGH))
    def _generate_catalog_frame(self) -> None:
        super(KDKDownloadFrame, self).__init__(None, title=self.title, size=(300, 200), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        gui_support.GenerateMenubar(self, self.constants).generate()
        self.Centre()
        title_label = wx.StaticText(self, label="Fetching KDKs", pos=(-1,5))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        title_label.Centre(wx.HORIZONTAL)
        progress_bar = wx.Gauge(self, range=100, pos=(-1, title_label.GetPosition()[1] + title_label.GetSize()[1] + 5), size=(250, 30))
        progress_bar.Centre(wx.HORIZONTAL)
        progress_bar_animation = gui_support.GaugePulseCallback(self.constants, progress_bar)
        progress_bar_animation.start_pulse()
        self.SetSize((-1, progress_bar.GetPosition()[1] + progress_bar.GetSize()[1] + 40))
        self.Show()
        def _fetch_installers():
            try:
                if self.constants.github_proxy_link!="Default":
                    KDK_API_LINK:str=KDK_API_LINK_PROXY
                else:
                    KDK_API_LINK: str = KDK_API_LINK_ORIGIN
                response = requests.get(KDK_API_LINK,verify=False)
                self.kdk_data = response.json()
                self.kdk_data_latest = []
                kdk_data_number=[]
                kdk_data_build=[]
                maxnx=[]
                for i in range(len(self.kdk_data)):
                    self.kdk_data[i]['seen']=((self.kdk_data[i]['seen']).split("T"))[0]
                    if self.constants.github_proxy_link!="SimpleHac" and self.constants.github_proxy_link!="Default":
                        self.kdk_data[i]['url']=self.kdk_data[i]['url'].replace("https://gitapi.simplehac.top/","")
                    if self.constants.github_proxy_link=="gh-proxy":
                        self.kdk_data[i]['url']="https://gh-proxy.com/"+self.kdk_data[i]['url']
                    if self.constants.github_proxy_link=="ghfast":
                        self.kdk_data[i]['url']="https://ghfast.top/"+self.kdk_data[i]['url']
                for i in range(len(self.kdk_data)):
                    data=self.kdk_data[i]["build"][:2]
                    data2=self.kdk_data[i]["build"]
                    kdk_data_number.append(data)
                    kdk_data_build.append(data2)
                for i in range(4):
                    maxn=kdk_data_number[0]
                    while True:
                        kdk_data_number.pop(0)
                        if len(kdk_data_number)==0 or kdk_data_number[0]<maxn :
                            break
                    maxnx.append(maxn)
                i=0
                fl=[0,0,0,0]
                while True:
                    if maxnx[0] == self.kdk_data[i]["build"][:2] and fl[0]==0:
                        self.kdk_data_latest.append(self.kdk_data[i])
                        fl[0]=1
                        i+=1
                    if  maxnx[1] == self.kdk_data[i]["build"][:2]and fl[1]==0:
                        self.kdk_data_latest.append(self.kdk_data[i])
                        fl[1]=1
                        i+=1
                    if  maxnx[2] == self.kdk_data[i]["build"][:2]and fl[2]==0:
                        self.kdk_data_latest.append(self.kdk_data[i])
                        fl[2]=1
                        i+=1
                    if  maxnx[3] == self.kdk_data[i]["build"][:2]and fl[3]==0:
                        self.kdk_data_latest.append(self.kdk_data[i])
                        fl[3]=1
                        i+=1
                    if i==len(self.kdk_data)-1:
                        break
                    else:
                        i+=1
                        continue
                self.kdk_data_full=self.kdk_data
                self.kdk_data_latest=self.kdk_data_latest
            except requests.RequestException as e:
                wx.MessageBox(f"Fetching KDK ERROR: {e}", "Error", wx.OK | wx.ICON_ERROR)
                self.on_return_to_main_menu()
        thread = threading.Thread(target=_fetch_installers)
        thread.start()
        gui_support.wait_for_thread(thread)
        progress_bar_animation.stop_pulse()
        progress_bar.Hide()
        self._display_available_installers()
    def convert_size(self,size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    def detect_os_build(self, rsr: bool = False) -> str:
        import plistlib
        file_path = "/System/Library/CoreServices/SystemVersion.plist"
        if rsr is True:
            file_path = f"/System/Volumes/Preboot/Cryptexes/OS{file_path}"
        try:
            return plistlib.load(open(file_path, "rb"))["ProductBuildVersion"]
        except Exception as e:
            raise RuntimeError(f"Failed to detect OS build: {e}")
    def _display_available_installers(self, event: wx.Event = None, show_full: bool = False) -> None:
        if show_full:
            self.show_fully=True
        else:
            self.show_fully=False
        self.os_build_tahoe=self.detect_os_build(False)
        bundles = [wx.BitmapBundle.FromBitmaps(self.icons)]
        self.frame_modal.Destroy()
        self.frame_modal = wx.Dialog(self, title="Choose KDK Version", size=(500, 580))
        title_label = wx.StaticText(self.frame_modal, label="Choose KDKs", pos=(-1,-1))
        title_label.SetFont(gui_support.font_factory(19, wx.FONTWEIGHT_BOLD))
        id = wx.NewIdRef()
        self.list = wx.ListCtrl(self.frame_modal, id, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER | wx.BORDER_SUNKEN)
        self.list.SetSmallImages(bundles)
        self.list.InsertColumn(0, "name",        width=160)
        self.list.InsertColumn(1, "version",      width=50)
        self.list.InsertColumn(2, "build",        width=75)
        self.list.InsertColumn(3, "size",         width=85)
        self.list.InsertColumn(4, "seen", width=105)
        if show_full is False:
            self.frame_modal.SetSize((500, 400))
        installers = self.kdk_data_latest[::-1] if show_full is False else self.kdk_data_full[::-1]
        if installers:
            locale.setlocale(locale.LC_TIME, '')
            logging.info(f"Available installers on Hackdoc ({'All entries' if show_full else 'Latest only'}):")
            xnu_name={
                "26":"Tahoe Beta",
                "15":"Sequoia",
                "14":"Sonoma",
                "13":"Ventura",
            }
            import re
            for item in installers:
                logging.info(f"- {item['name']} (macOS {item['version']} - {item['build']}):\n  - Size: {self.convert_size(item['fileSize'])}\n  - Link: {item['url']}\n")
                version = re.search(r'^\d+', item['version'])
                index = self.list.InsertItem(self.list.GetItemCount(), f"macOS {xnu_name[version.group()]}")
                self.list.SetItemImage(index, 0)
                self.list.SetItem(index, 1, f"{item['version']}")
                self.list.SetItem(index, 2, f"{item['build']}")
                self.list.SetItem(index, 3, f"{self.convert_size(item['fileSize'])}")
                self.list.SetItem(index, 4, f"{item['seen']}")
        else:
            logging.error("Cannot find any KDKs on Github")
            wx.MessageDialog(self.frame_modal, "Failed to download KDKs Catalog from Hackdoc", "Error", wx.OK | wx.ICON_ERROR).ShowModal()
            self.on_return_to_main_menu()
        if show_full is False:
            self.list.Select(-1)
        self.list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_select_list)
        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select_list)
        self.select_button = wx.Button(self.frame_modal, label="Download", pos=(-1, -1), size=(150, -1))
        self.select_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.select_button.Bind(wx.EVT_BUTTON, lambda event, installers=installers: self.on_download_installer(installers))
        self.select_button.SetToolTip("Choose KDKs")
        self.select_button.SetDefault()
        if show_full is True:
            self.select_button.Disable()
        self.copy_button = wx.Button(self.frame_modal, label="Copy Link", pos=(-1, -1), size=(80, -1))
        self.copy_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        if show_full is True:
            self.copy_button.Disable()
        self.copy_button.SetToolTip("Copy KDK Download Link")
        self.copy_button.Bind(wx.EVT_BUTTON, lambda event, installers=installers: self.on_copy_link(installers))
        return_button = wx.Button(self.frame_modal, label="Return to Main Menu", pos=(-1, -1), size=(150, -1))
        return_button.Bind(wx.EVT_BUTTON, self.on_return_to_main_menu)
        return_button.SetFont(gui_support.font_factory(13, wx.FONTWEIGHT_NORMAL))
        self.showolderversions_checkbox = wx.CheckBox(self.frame_modal, label="Show Older/Beta Versions", pos=(-1, -1))
        if show_full is True:
            self.showolderversions_checkbox.SetValue(True)
        self.showolderversions_checkbox.Bind(wx.EVT_CHECKBOX, lambda event: self._display_available_installers(event, self.showolderversions_checkbox.GetValue()))
        if self.os_build_tahoe!='25A5316i':
            rectbox = wx.StaticBox(self.frame_modal, -1)
            rectsizer = wx.StaticBoxSizer(rectbox, wx.HORIZONTAL)
            rectsizer.Add(self.copy_button, 0, wx.EXPAND | wx.RIGHT, 5)
            rectsizer.Add(self.select_button, 0, wx.EXPAND | wx.LEFT, 5)
        checkboxsizer = wx.BoxSizer(wx.HORIZONTAL)
        checkboxsizer.Add(self.showolderversions_checkbox, 0, wx.ALIGN_CENTRE | wx.RIGHT, 5)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddSpacer(10)
        sizer.Add(title_label, 0, wx.ALIGN_CENTRE | wx.ALL, 0)
        sizer.Add(self.list, 1, wx.EXPAND | wx.ALL, 10)
        if self.os_build_tahoe!='25A5316i':
             sizer.Add(rectsizer, 0, wx.ALIGN_CENTRE | wx.ALL, 0)
             sizer.AddSpacer(8)
        elif self.os_build_tahoe=='25A5316i':
            mosizer=wx.BoxSizer(wx.HORIZONTAL)
            mosizer.Add(self.copy_button, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
            mosizer.Add(self.select_button, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
            sizer.Add(mosizer, 0, wx.ALIGN_CENTRE | wx.ALL, 0)
            sizer.AddSpacer(8)
        sizer.Add(checkboxsizer, 0, wx.ALIGN_CENTRE | wx.ALL, 15)
        sizer.Add(return_button, 0, wx.ALIGN_CENTRE | wx.BOTTOM, 15)
        self.frame_modal.SetSizer(sizer)
        self.frame_modal.ShowWindowModal()
    def on_copy_link(self, installers: dict) -> None:
        selected_item = self.list.GetFirstSelected()
        if selected_item != -1:
            clipboard = wx.Clipboard.Get()
            if not clipboard.IsOpened():
                clipboard.Open()
            clipboard.SetData(wx.TextDataObject(installers[selected_item]['url']))
            clipboard.Close()
            wx.MessageDialog(self.frame_modal, "Download link copied to clipboard", "", wx.OK | wx.ICON_INFORMATION).ShowModal()
    def on_select_list(self, event):
        if self.list.GetSelectedItemCount() > 0:
            self.select_button.Enable()
            self.copy_button.Enable()
        else:
            self.select_button.Disable()
            self.copy_button.Disable()   
    def on_download_installer(self, installers: dict,retry:bool=False) -> None:
        if retry and self.backup_item is not None:
            selected_installer=self.backup_item
        else:
            selected_item = self.list.GetFirstSelected()
        if selected_item != -1 or retry:
            if retry and self.backup_item is not None:
                selected_installer=self.backup_item
            else:
                selected_installer = installers[selected_item]
            def is_dir_writable(dirpath):
                    import os
                    return os.access(dirpath, os.W_OK | os.X_OK)
            if not is_dir_writable(self.constants.user_download_file):
                import getpass
                self.constants.user_download_file=f"/Users/{getpass.getuser()}/Downloads"
            self.validate_ins=selected_installer
            self.backup_item=selected_installer
            file_name = selected_installer['name']+".dmg"
            self.frame_modal.Close()
            self.path_validate=self.constants.user_download_file+"/"+file_name
            size=selected_installer['fileSize']
            download_obj = network_handler.DownloadObject(selected_installer['url'], self.constants.user_download_file+"/"+file_name,self.convert_size(size))
            gui_download.DownloadFrame(
                self,
                title=self.title,
                global_constants=self.constants,
                download_obj=download_obj,
                item_name=f"KDK {selected_installer['version']} {selected_installer['build']}",
                download_icon=str(self.constants.icns_resource_path / "Package.icns")
            )
            if download_obj.download_complete is False:
                import os
                os.remove(self.constants.user_download_file+"/"+file_name)
                self.on_return_to_main_menu()
                return
            self.on_return_to_main_menu()
    def on_download(self) -> None:
        self.frame_modal.Close()
        self.parent.Hide()
        self._generate_catalog_frame()
        self.parent.Close()
    def on_return_to_main_menu(self, event: wx.Event = None) -> None:
        if self.frame_modal:
            self.frame_modal.Hide()
        main_menu_frame = gui_main_menu.MainFrame(
            None,
            title=self.title,
            global_constants=self.constants,
            screen_location=self.GetScreenPosition()
        )
        main_menu_frame.Show()
        if self.frame_modal:
            self.frame_modal.Destroy()
        self.Destroy()
    