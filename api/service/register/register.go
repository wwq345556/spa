package register

import (
	"errors"
	"spa/api/helper"
	"spa/api/models/request"
	"spa/api/models/user"
	"strings"
	"time"
)

func Register(params *request.User) error {


	num,err := user.CheckPhone(params.Phone)
	if num == 1 {
		return errors.New("该手机号码已被注册")
	}
	if err != nil {
		return err
	}

	pwd := strings.EqualFold(params.Password, params.Pwd)
	if !pwd {
		return errors.New("两次输入不相同")
	}

	password := helper.MD5(params.Password)
	var userInfo = new(user.User)
	userInfo.Name = params.Name
	userInfo.Password = password
	userInfo.Phone = params.Phone
	userInfo.Create_time = time.Now().Unix()
	err = user.Register(userInfo)

	return err
}
