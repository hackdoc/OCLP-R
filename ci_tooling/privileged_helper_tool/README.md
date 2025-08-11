# OCLP-R Privileged Helper Tool

`com.pyquick.oclp-r.privileged-helper` is OCLP-R's Privileged Helper Tool.

The architecture is as such:
1. The main application (OCLP-R.app) will send arguments to the privileged helper tool to execute.
2. The privileged helper tool will check the code signature of the main application to ensure it is signed by pyquick.
3. The privileged helper tool will then execute the command and return the output to the main application.

The helper tool is able to execute code as root by using the "Set UID" bit present on the file.


## Running from source

Since running OCLP-R from source will lack pyquick's code signature, you will need to disable code signature verification in the privileged helper tool otherwise root commands will fail.

To do so, compile the privileged helper tool with debug:
```
make debug
```

Then when you build OCLP-R.pkg, the debug version of the helper tool will be used.


### Security Considerations

When using the Privileged Helper Tool from source, you are now adding a security risk to your system. By disabling the code signature checks, any malicious application is given ability to execute code as root.

If possible, we highly recommend creating a developer account with Apple and signing the application with your own ["Developer ID Application" certificate](https://developer.apple.com/help/account/create-certificates/create-developer-id-certificates/). This will allow you to run the application without disabling code signature checks.

* Note that pyquick's Team ID will need to be replaced in main.m with your own Team ID (`S74BDJXQMD` -> `YOUR_TEAM`)
* Additionally you will be required to compile OCLP-R.app with your own Developer ID Application certificate

If this is not possible, we recommend using [OCLP-R's prebuilt binaries](../../SOURCE.md) instead.