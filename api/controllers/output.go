package controllers

type Output struct {
	Code int `json:"code"`
	Msg  string `json:"msg"`
	Data interface{} `json:"data"`
}

const (
	SuccessCode = 1
	ErrorCode   = 0
)

const(
	SuccessMsg = "操作成功"
	ErrorMsg   = "系统异常"
)

var DefaultErrorMsgList = map[string]string{
	"<QuerySeter> no row found": "未知数据",	
}

//返回成功
func (output *Output) SuccessOutput (data interface{},msg string) *Output {
	output.Code = SuccessCode
	if msg == "" {
		output.Msg = SuccessMsg
	} else {
		output.Msg = msg
	}
	output.Data = data
	return output
}

//返回失败
func (output *Output) ErrorOutput(msg string) *Output {
	output.Code = ErrorCode
	if msg == "" {
		output.Msg = ErrorMsg
	} else {
		output.Msg = output.SetDefaultErrorMsg(msg)
	}
	return output
}

//获取error默认提示信息
func (output * Output) SetDefaultErrorMsg(errorMsg string) string {
	if DefaultErrorMsgList[errorMsg] != "" {
		return DefaultErrorMsgList[errorMsg] 
	}
	return errorMsg
}