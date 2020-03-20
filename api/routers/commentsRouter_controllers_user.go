package routers

import (
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/context/param"
)

func init() {

    beego.GlobalControllerRouter["spa/api/controllers/user:UserInformationController"] = append(beego.GlobalControllerRouter["spa/api/controllers/user:UserInformationController"],
        beego.ControllerComments{
            Method: "Register",
            Router: `register`,
            AllowHTTPMethods: []string{"post"},
            MethodParams: param.Make(),
            Filters: nil,
            Params: nil})

}
