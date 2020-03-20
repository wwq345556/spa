package main

import (
	_ "spa/api/routers"
	_ "spa/api/models"
	"github.com/astaxie/beego"
)

func main() {
	beego.Run()
}

