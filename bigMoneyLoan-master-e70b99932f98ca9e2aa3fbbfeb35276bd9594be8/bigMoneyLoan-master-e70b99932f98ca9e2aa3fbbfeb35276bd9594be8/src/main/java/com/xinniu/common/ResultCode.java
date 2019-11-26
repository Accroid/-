package com.xinniu.common;

import java.io.Serializable;

/**
 * Created by sunjinghai on 2018/7/27.
 */
public class ResultCode {
    public static final int NO_AUTHORITY = 10001;               //当前用户无权限操作
    public static final int CAPITAL_CIPHER_ERR = 10002;         //资金密码错误
    public static final int GET_USER_INFO_ERR = 10003;          //获取用户信息失败
    public static final int PASSWORD_REPAT_ERR = 10004;         //登录密码不可与资金密码一致
    public static final int NO_CHAT_GROUP = 10005;              //聊天群组已不存在
    public static final int GET_GROUP_MEMBER_ERR = 10006;       //获取群组成员失败
    public static final int ADD_GROUP_MEMBER_ERR = 10007;       //添加群组成员失败
    public static final int ADDRESS_ERR = 10008;                //地址不正确
    public static final int POSITIVE_MONEY_ERR = 10009;         //金额需为正数
    public static final int NOT_ENOUGH_ERR = 10010;             //用户可用资金不足
    public static final int ALREADY_DEAL = 10011;               //该订单已处理
    public static final int NOT_ENOUGH_FROZEN_GOODS = 10012;    //商品的冻结数量不足
    public static final int NOT_ENOUGH_FROZEN_MONEY = 10013;    //用户冻结资金不足
    public static final int ALREADY_REGISTER = 10014;           //该用户已注册
    public static final int NO_USER = 10015;                    //该用户不存在
    public static final int OTC_NOT_REGISTER = 10016;           //OTC未注册
    public static final int CAPTCHA_EXPIRED = 10017;            //验证码已过期
    public static final int CAPTCHA_ERR = 10018;                //验证码不正确
    public static final int IDENTITY_ALREADY_USED = 10019;      //该证件已用于实名认证
    public static final int IDENTITY_CODE_ERR = 10020;          //身份证号码不正确
    public static final int SHIELD_SELF_ERR = 10021;            //不能屏蔽自己
    public static final int APPEAL_TIME_ERR = 10022;            //付款成功后5分钟才可以发起申诉
    public static final int EDIT_COMMODITY_ERR = 10023;         //您有广告在发布，无法修改账户
    public static final int FEE_CALCULATE_ERR = 10024;          //手续费计算失败
    public static final int POSITIVE_QUANTITY_ERR = 10025;      //数量需为正数
    public static final int POSITIVE_PRICE_ERR = 10026;         //价格需为正数
    public static final int PRICE_AREA_ERR = 10027;             //浮动价格区间不合理
    public static final int PAYMENT_ERR = 10028;                //非法的支付方式
    public static final int CANCEL_ORDER_OVER = 10029;          //取消交易次数过多，交易权限24小时内受限
    public static final int COMMODITY_OFFLINE = 10030;          //商品已下架
    public static final int BUY_SELF_ERR = 10031;               //不能购买自身发布的商品
    public static final int NOT_ENOUGH_GOODS = 10032;           //商品的数量不足
    public static final int COMMODITY_UPDATED = 10033;          //该订单商家已修改价格
    public static final int NOT_IDENTITY = 10034;               //您尚未实名认证
    public static final int NO_PAYMENT_ERR = 10035;             //您需要添加支付方式
    public static final int PASSWORD_ERR = 10036;               //登录密码错误

    public static final int ORDER_COUNT_LIMIT = 20001;          //交易笔数要大于XX次
    public static final int CAPITAL_CIPHER_ERR_EXTEND = 20002;  //资金密码错误，还剩余XX次

    public static final int SUCCESS = 0;                        //成功
    public static final int UN_KNONW_ERROR = 1000;              //服务器开了小差，请稍候重试
    public static final int DB_ERROR = 1002;                    //数据库操作异常
    public static final int DB_TIMEOUT = 1003;                  //数据库访问超时
    public static final int NETWORK_EXP = 1004;                 //网络异常
    public static final int EXTERNAL_SERVICE__EXP = 1005;       //外部服务器异常
    public static final int EXTERNAL_SERVICE_TIMEOUT = 1006;    //外部服务器超时
    public static final int API_OVERDUE = 1007;                 //API已过期
    public static final int METHOD_UN_IMPL = 1008;              //当前操作未实现


    public static final int JSONP_NOT_SUP = 1009;               //不支持Jsonp请求
    public static final int ILLEGAL_REQ = 1010;                 //非法请求
    public static final int INVALID_OP = 1011;                  //无效操作
    public static final int DATA_ERR = 2000;                    //数据错误
    public static final int DATA_EXIST = 2002;                  //数据已存在
    public static final int DATA_FORMAT_ERR = 2003;             //数据格式错误
    public static final int DATA_TYPE_ERR = 2004;               //数据类型错误
    public static final int DATA_REPAT_ERR = 2005;              //数据重复
    public static final int DATA_UN_ACCESS = 2006;              //数据没有授权
    public static final int PARA_ERR = 3000;                    //参数错误
    public static final int PARA_MISSING_ERR = 3002;            //缺少参数
    public static final int PARA_NIL = 3003;                    //参数不能为空值
    public static final int PARA_FORMAT_ERR = 3004;             //参数格式错误
    public static final int PARA_OUT_RANGE = 3005;              //参数值超出允许范围
    public static final int TOKEN_INVALID = 3006;               //令牌无效
    public static final int TOKEN_IS_USE = 3007;                //令牌已使用
    public static final int TOKEN_TIMEOUT = 3008;               //令牌过期
    public static final int SIGNATURE_INVALID = 3009;           //签名无效
    public static final int TIME_OUT_RANGE = 3010;              //时间戳超出允许范围
    public static final int CHR_ILLEGAL = 3011;                 //存在非法字符
    public static final int PARA_OUT_LEN = 3012;                //参数值长度超过限制
    public static final int HAS_SUBTLE = 3013;                  //存在有敏感词
    public static final int SIGNATURE_ERROR = 3014;             //签名错误
    public static final int CAPTCHA_ERROR = 3015;               //验证码错误
    public static final int ACCESS_DENIED = 4000;               //无权限
    public static final int NOT_LOG = 4002;                     //未登录
    public static final int IP_LIMIT = 4003;                    //IP限制
    public static final int DATA_NOT_EXIST = 2007;              //数据不存在
    public static final int API_ACCESS_DENIED = 4004;           //API未授权
    public static final int HYSTRIX_TIMEOUT = 5000;             //服务连接超时
    public static final int HYSTRIX_IO_ERROR = 5001;            //服务还未启动成功
    public static final int HYSTRIX_ERROR = 5002;               //没有可调用服务
    public static final int RIBBON_TIMEOUT = 5003;              //服务连接超时
    public static final int RIBBON_IO_ERROR = 5004;             //服务还未启动成功
    public static final int RIBBON_ERROR = 5005;                //没有可调用服务
}
