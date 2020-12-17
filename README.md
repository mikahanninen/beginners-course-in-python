# Beginner's Course implemented in Python

https://robocorp.com/docs/courses/beginners-course

## Process description

Process is split into 2 steps. First step, `downloadTask`, downloads Excel file which is read and
stored in list format into work item variable. Second step, `processingTask`, reads the work item variable
content and goes through each item in the list variable.

The `processingTask` is run by default in _headless_ mode, but UI can be set visible by setting environment variable `SHOW_UI` to any value.

## To run in development

These steps describe how to use Robocorp Cloud Vault and
local workitems file for development runs.

Note. This is not necessary if process is run only in the Cloud.

1. create folder `devdata` into task root folder (this folder is in `.gitignore` file)
2. create empty `workitems.json` file into `devdata` folder
3. create `env.json` into `devdata` folder with following content

    ```{
        "RC_WORKSPACE_ID": "MY_WORKSPACE_ID",
        "RC_API_SECRET_HOST": "https://api.eu1.robocloud.eu",
        "RC_API_SECRET_TOKEN": "MY_AUTH_TOKEN",
        "RC_WORKITEM_ID": "MY_WORKSPACE_ID",
        "RPA_WORKITEMS_ADAPTER": "RPA.Robocloud.Items.FileAdapter",
        "RPA_WORKITEMS_PATH": "./devdata/workitems.json"
    }```
    
4. replace `MY_WORKSPACE_ID` parts with your ID from output from command: `rcc cloud workspace`
5. replace `MY_AUTH_TOKEN` with output from command: `rcc cloud authorize -w <MY_WORKSPACE_ID>`

## Running in command line

Execute the run command: `rcc run -e devdata/env.json -t downloadTask`

## Running in Robocorp Lab

   1. in Lab terminal - execute the run command: `rcc run -t downloadTask`
   2. using notebook mode `Restart Kernel and Run All Cells`
   3. using `Run Robot` button

## Running in Visual Studio Code

    1. use terminal and run with rcc like mentioned above
    2. run using `Robocorp Code` extension

## Links

https://forum.robocorp.com/t/is-it-possible-to-have-a-locally-run-robot-fetch-secrets-from-robocorp-cloud-vault/297
