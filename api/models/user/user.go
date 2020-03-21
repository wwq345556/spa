package user

import (
	"github.com/astaxie/beego/orm"
)

type User struct {
	Id int `orm:"column(id);auto" description:"ID" `
	Name string `orm:"column(name)" description:"姓名"`
	Nickname string `orm:"column(nickname)" description:"昵称"`
	Phone string `orm:"column(phone)" description:"电话"`
	Password string `orm:"column(password)" description:"密码"`
	Is_del int8 `orm:"column(is_del)" description:"是否删除"`
	Create_time int64 `orm:"column(create_time)" description:"创建时间"`
	Update_time int64 `orm:"column(update_time)" description:"修改时间"`
	Delete_time int64 `orm:"column(delete_time)" description:"删除时间"`
}

func init() {
	orm.RegisterModel(new(User))
}

func Register(params *User) error {
	db := orm.NewOrm()
	_, err := db.Insert(params)
	return err
}

func CheckPhone(phone string) (int,error) {
	var num int
	db := orm.NewOrm()
	err := db.Raw(`select count(*) from user where phone = ?`,phone).QueryRow(&num)
	return num,err
}
