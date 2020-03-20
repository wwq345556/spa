package controllers

import (
	"fmt"
	"github.com/astaxie/beego"
	"github.com/astaxie/beego/validation"
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

//通过结构体获取数据
func (controller *CommonController) GetParamStruct(paramsStruct interface{}) {
	if err := controller.ParseForm(paramsStruct); err != nil {
		controller.Fail(err.Error())
	}
	controller.CheckValidation(paramsStruct)
}

//validation验证， error直接返回
func (controller *CommonController) CheckValidation(requestData interface{}) {
	valid := validation.Validation{}
	res, err := valid.Valid(requestData)
	if err != nil {
		controller.Fail(err.Error())
	}
	//包含错误信息
	if !res {
		errors := ""
		for _,err := range valid.Errors {
			errors += fmt.Sprintf("%s:%s", err.Key, err.Message)
		}
		controller.Fail(errors)
	}
}
