package user

import (
	"spa/api/controllers"
)

type UserInformationController struct {
	controllers.CommonController
}
// @router get [get]
func (this *UserInformationController) Get() {
	this.Fail("000")
}