package user

import (

	"spa/api/controllers"
	"spa/api/models/request"
	"spa/api/service/register"
)

type UserInformationController struct {
	controllers.CommonController
}
// @router register [post]
func (this *UserInformationController) Register() {
	request := new(request.User)
	this.GetParamStruct(request)
	err := register.Register(request)
	if err != nil {
		this.CheckError(err,"")
	}

	this.Success("","操作成功")
}