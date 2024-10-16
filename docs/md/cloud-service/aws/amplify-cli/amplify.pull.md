
# amplify pull

deploy されている 実行環境上の src を cloud9 に 落として配置する


## 基本

```
amplify pull
```


## 初回実行, および 設定

初回実行時に 引数なしで実行で, 紐づける project などの 設定を行うことができる

```
amplify pull
```

ex

```
_ amplify pull
? Select the authentication method you want to use: AWS profile

For more information on AWS Profiles, see:
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

? Please choose the profile you want to use default
? Which app are you working on? xxxxxxxxxxxxx
? Pick a backend environment: dev
? Choose your default editor: Visual Studio Code
✔ Choose the type of app that you're building · javascript
Please tell us about your project
? What javascript framework are you using react
? Source Directory Path:  src
? Distribution Directory Path: build
? Build Command:  npm run-script build
? Start Command: npm run-script start
? Do you plan on modifying this backend? Yes
⠙ Fetching updates to backend environment: dev from the cloud.⠋ Building resource xxxxxx✔ Successfully pulled backend environment dev from the cloud.
✅

✅ Successfully pulled backend environment dev from the cloud.
Run 'amplify pull' to sync future upstream changes.
```

`? Which app are you working on? xxxxxxxxxxxxx` の line で prj を setting している



## question

q. pull 先の紐づきはどこで設定している ?

a. amplify pull の初回実行で設定する
- `amplify env checkout env_name`
  - `amplify env list` で確認



