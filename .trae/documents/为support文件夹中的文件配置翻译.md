# 为support文件夹中的文件配置翻译

## 目标
为support文件夹中所有未配置翻译的文件创建对应的翻译函数，每个文件对应一个翻译函数。

## 已完成的翻译函数
- arguements.py → arguements()
- defaults.py → defaults()
- generate_smbios.py → generate_smbios()
- global_settings.py → global_settings()
- install.py → install()
- integrity_verification.py → integrity_verification()
- kdk_handler.py → kdk_handler()

## 需要添加的翻译函数
1. analytics_handler.py → analytics_handler()
2. commit_info.py → commit_info()
3. logging_handler.py → logging_handler()
4. macos_installer_handler.py → macos_installer_handler()
5. metallib_handler.py → metallib_handler()
6. network_handler.py → network_handler()
7. private.py → private()
8. reroute_payloads.py → reroute_payloads()
9. subprocess_wrapper.py → subprocess_wrapper()
10. updates.py → updates()
11. utilities.py → utilities()
12. validation.py → validation()

## 实现步骤
1. 为每个需要翻译的文件创建一个对应的翻译函数
2. 每个翻译函数包含英文和中文两种语言的翻译字典
3. 翻译字典包含该文件中所有需要翻译的文本
4. 保持与现有翻译函数相同的格式和结构

## 注意事项
- 每个翻译函数的命名格式为：`def 文件名():`
- 翻译字典中键为英文文本，值为对应语言的翻译
- 对于中文语言点(language_point==0)，提供中文翻译
- 对于英文语言点(language_point==1)，保持英文原文
- 确保所有需要翻译的文本都被包含在翻译字典中
- 保持代码格式一致，使用相同的缩进和换行格式