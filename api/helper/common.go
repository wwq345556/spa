package helper

import (
	"crypto/md5"
	"encoding/hex"
)

func MD5(pwd string) string {
	mdc := md5.New()
	mdc.Write([]byte(pwd))
	enPwd := hex.EncodeToString(mdc.Sum(nil))
	return enPwd
}
