package controllers

import (
	"github.com/astaxie/beego"
)

type CommonController struct {
	beego.Controller
}

// 成功返回json
func (controller *CommonController) Success(data interface{}, msg string) {
	controller.Data["json"] = new(Output).SuccessOutput(data, msg)
	controller.ServeJSON()
	controller.StopRun()
}

//失败返回json
func (controller *CommonController) Fail(msg string) {
	controller.Data["json"] = new(Output).ErrorOutput(msg)
	controller.ServeJSON()
	controller.StopRun()
}
