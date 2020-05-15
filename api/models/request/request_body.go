package request

//用户信息(注册登录)
type User struct {
	Name string `form:"name"`
	Phone string `form:"phone"`
	Password string `form:password`
	Pwd string `form:pwd`
}