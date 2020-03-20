package request

//用户信息(注册登录)
type User struct {
	Name string `from:"name"`
	Phone string `from:"phone"`
	Password string `from:password`
	Pwd string ``
}