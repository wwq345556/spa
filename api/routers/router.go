package routers

import (
	"github.com/astaxie/beego"
	"spa/api/controllers/user"
)

func init() {
	//初始化 namespace
	ns :=
	beego.NewNamespace("/v1",
    	beego.NSNamespace("/user",
        	beego.NSInclude(
            	&user.UserInformationController{},
        	),
    	),
	)
	//注册 namespace
	beego.AddNamespace(ns)
    // beego.Router("/", &controllers.MainController{})
}
