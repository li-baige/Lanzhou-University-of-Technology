# 2021   兰州疫情可视化-react版本

## 功能

   - 确诊人员信息
   - 病例行程轨迹
   - 封禁小区数据
   
## 预览
 
   ![首页](/docs/image/%E9%A6%96%E9%A1%B5.png) 
   ![市级数据](/docs/image/%E5%85%B0%E5%B7%9E.png)
   ![区级数据](/docs/image/%E4%B8%83%E9%87%8C%E6%B2%B3.png)
   ![封闭小区数据](/docs/image/%E5%BD%AD%E5%AE%B6%E5%9D%AA.png)
   ![确诊人员信息](/docs/image/%E7%A1%AE%E8%AF%8A%E4%BA%BA%E5%91%98%E4%BF%A1%E6%81%AF%20%E2%80%93%201.png)
   ![病患行程轨迹](/docs/image/%E7%97%85%E6%82%A31%E8%BD%A8%E8%BF%B9%E8%B7%AF%E7%BA%BF.png)

## 工程结构

   |--backend -----------------------------后端<br>
      --.idea<br>
      --.vscode<br>
      --APP -----------------------------接口<br>
      --data -----------------------------数据样本<br> 
      --server<br>
      --templates<br>
      --__init__.py -----------------------------兼容Mysql<br>
      --接口说明.md<br>
      --数据库测试.py<br>
      --db.sqlite3<br>
      --manage.py -----------------------------Django项目管理<br>
   |--docs <br>
      --image -----------------------------UI图<br>
      --数据库设计文档<br>
      --设计<br>
   |--frontend -----------------------------前端<br>
      --app<br> 
      --build<br>
      --node_modules<br>
      --public<br>
      --src<br>
        --pages -----------------------------页面组件<br>
          --Applayout.jsx -----------------------------框架组件<br>
          --Community.jsx -----------------------------社区组件<br>
          --Firstpagenew.jsx -----------------------------首页组件<br>
          --Information.jsx -----------------------------信息组件<br>
          --Path.jsx -----------------------------路劲组件<br>
          --Selfinfo.jsx -----------------------------个人信息组件<br>
        --routers -----------------------------路由<br>
      --gitignore<br>
      --package-lock.json<br>
      --package.json<br>
      --yarn-earn.log<br>
      --yarn.lock<br>
   |--README.md<br>
      

      
## 部署
   
### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

   

## 数据来源
- 丁香园
- 甘肃省疫情疾控中心
