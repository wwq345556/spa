package routers

import (
	"spa/api/controllers"
	"github.com/astaxie/beego"
)

func init() {
	//初始化 namespace
	ns :=
	beego.NewNamespace("/v1",
    	beego.NSNamespace("/cms",
        	beego.NSInclude(
            	&controllers.MainController{},
        	),
    	),
	)
	//注册 namespace
	beego.AddNamespace(ns)
    // beego.Router("/", &controllers.MainController{})
}
