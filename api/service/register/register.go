package register

import (
	"errors"
	"spa/api/helper"
	"spa/api/models/request"
	"spa/api/models/user"
	"strings"
	"time"
)

func Register(param *request.User) error {
	pwd := strings.EqualFold(param.Password, param.Pwd)
	if !pwd {
		return errors.New("两次输入不相同")
	}

	password := helper.MD5(param.Password)
	var userInfo = new(user.User)
	userInfo.Name = param.Name
	userInfo.Password = password
	userInfo.Phone = param.Phone
	userInfo.Create_time = time.Now().Unix()
	err := user.Register(userInfo)

	return err
}
