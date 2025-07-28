
# amplify configure


主に user ( iam ) を設定する


## 基本

```
amplify configure
```

ex

```
_ amplify configure
Follow these steps to set up access to your AWS account:

Sign in to your AWS administrator account:
https://console.aws.amazon.com/
Press Enter to continue
Unable to open https://console.aws.amazon.com/: spawn xdg-open ENOENT
Have you installed `xdg-utils` on your machine?

Specify the AWS Region
? region:  ap-northeast-1
Follow the instructions at
https://docs.amplify.aws/cli/start/install/#configure-the-amplify-cli

to complete the user creation in the AWS console
https://console.aws.amazon.com/iamv2/home#/users/create
Press Enter to continue
Unable to open https://docs.amplify.aws/cli/start/install/#configure-the-amplify-cli: spawn xdg-open ENOENT
Have you installed `xdg-utils` on your machine?
Unable to open https://console.aws.amazon.com/iamv2/home#/users/create: spawn xdg-open ENOENT
Have you installed `xdg-utils` on your machine?

Enter the access key of the newly created user:
? accessKeyId:  ********************
? secretAccessKey:  ****************************************
This would update/create the AWS Profile in your local machine
? Profile Name:  default

Successfully set up the new user.
```



