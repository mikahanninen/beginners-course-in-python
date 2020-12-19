# Robot Spare Bin Intranet Robot - Python implementation

This example robot solves the use case which is examined in Robocorp's Beginners course. Instead of using Robot Framework, it demonstrates a full Python implementation.

You can follow the course here: https://robocorp.com/docs/courses/beginners-course

## Process description

The process is split into two steps.

- The first step, `downloadTask`, downloads the Excel source data file, reads it, and stores its data into a work item variable.
- The second step, `processingTask`, reads the workitem variable content and processes each item, filling the sales form on the website.

The `processingTask` is run by default in _headless_ mode, but the UI can be made visible by setting the environment variable `SHOW_UI` to any value.

The main process output is stored into the `output/sales.zip` file, which contains all images and PDFs created during the `processingTask` step.
Please note that the `Output` directory has been added to the `.gitignore` file, and so it is not present in this repository.

## Libraries used

This example makes use of the [RPA framework](/product-manuals/rpa-framework/rpa-framework-overview) set of libraries, which can be used either in Robot Framework or Python.

### RPA Framework libraries used in the `downloadTask` step

- RPA.Excel.Files
- RPA.FileSystem
- RPA.HTTP
- RPA.Robocloud.Items

### RPA Framework libraries used in the `processingTask` step

- RPA.Archive
- RPA.Browser
- RPA.FileSystem
- RPA.PDF
- RPA.Robocloud.Secrets
- RPA.Robocloud.Items

## Robocorp Cloud set up

You will need to upload this robot to Robocorp cloud, and to create a process with the two steps contained in the robot in your Workspace. You can find instructions [here](https://robocorp.com/docs/product-manuals/robocorp-cloud/configuring-robots-for-running-in-robocorp-cloud).

### Robocorp Vault

This robot makes use of the Robocloud Vault feature to store the access credentials to access a web application.

Create a secret called `salessite`, containing secrets for `username` and `password`.
You can find the credentials [on the Beginners' course site](https://robocorp.com/docs/courses/beginners-course/logging-in#filling-and-submitting-the-form).

## Local run set up

Follow these steps to use describe how to use Robocorp Cloud Vault and local workitems file for development runs.

By following these steps, you can run the robot locally. You will:

- use your remote [vault on Robocorp Cloud](/development-howtos/variables-and-secrets/vault) (Read more about this approach here: https://forum.robocorp.com/t/is-it-possible-to-have-a-locally-run-robot-fetch-secrets-from-robocorp-cloud-vault/297)
- use a local file to define [work items](/product-manuals/robocorp-cloud/using-robocloud-items-library#what-is-the-work-item)

> Note: These steps are only necessary when running the process locally

1. create a directory with name `devdata` into the task root directory (this directory is added to the `.gitignore` file)
2. create an empty `workitems.json` file inside the `devdata` directory
3. create an empty `env.json` file inside the `devdata` directory, with the following content:

```
    {
        "RC_WORKSPACE_ID": "MY_WORKSPACE_ID",
        "RC_API_SECRET_HOST": "https://api.eu1.robocloud.eu",
        "RC_API_SECRET_TOKEN": "MY_AUTH_TOKEN",
        "RC_WORKITEM_ID": "MY_WORKSPACE_ID",
        "RPA_WORKITEMS_ADAPTER": "RPA.Robocloud.Items.FileAdapter",
        "RPA_WORKITEMS_PATH": "./devdata/workitems.json"
    }
```

4. replace `MY_WORKSPACE_ID` with the ID of your workspace. You can find the id using the command `rcc cloud workspace`, or on the workspace settings page in Robocorp Cloud.
5. replace `MY_AUTH_TOKEN` with the output from the command: `rcc cloud authorize -w <MY_WORKSPACE_ID>`

## Running in command-line

Execute the run commands:

- `rcc run -e devdata/env.json -t downloadTask` for the first step
- `rcc run -e devdata/env.json -t processingTask` for the second step

## Running in Visual Studio Code

You can run this robot easily usign the [Robocorp VS Code extension]: https://robocorp.com/docs/product-manuals/robocorp-code#running-the-robot

## Running in Robocorp Lab

You have three different options:

- using notebook mode: click on the `>>` button, which executes `Restart Kernel and Run All Cells`
- click on the `Run Robot` button and select the step you want to run
- in Lab terminal: execute the run command: `rcc run -t downloadTask` and then `rcc run -t processingTask`
