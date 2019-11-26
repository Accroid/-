package com.xinniu.common;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;
import java.util.UUID;

/**
 * Created by sunjinghai on 2018/6/13.
 */
public class DataHouse {

    public static String getIdentityNumber() {
        CreateIdentityNumber createIdentityNumber = new CreateIdentityNumber();
        return createIdentityNumber.generate();
    }

    public static String getPhoneNumber() {
        String time = System.currentTimeMillis() + "";
        String phoneNumber = time.substring(0, 3) + time.substring(5, 13);
//        if(phoneNumber.substring(0,4).equals("154")){
        phoneNumber = phoneNumber.replace("154", "158");
//        }
        return phoneNumber;
    }

    public static String getEmail() {
        String time = System.currentTimeMillis() + "";
        return time + "@abc.cn";
    }

    public static String getNickName(int count) {
        String string = "0123456789ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        Random random = new Random();
        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < random.nextInt(10) + 10; ++i) {
            int number = random.nextInt(61);
            stringBuffer.append(string.charAt(number));
        }
        return stringBuffer.toString().substring(0, count);
    }

    public static String getMd5(String string) {
        MessageDigest md5 = null;
        try {
            md5 = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        string = "www.yztz.com#1Pwd_salt@Default2+!`%Ok_here'The&End$" + string;
        try {
            md5.update(string.getBytes("UTF-8"));
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        byte[] encryption = md5.digest();
        StringBuffer strBuf = new StringBuffer();
        for (int i = 0; i < encryption.length; i++) {
            if (Integer.toHexString(0xff & encryption[i]).length() == 1) {
                strBuf.append("0").append(Integer.toHexString(0xff & encryption[i]));
            } else {
                strBuf.append(Integer.toHexString(0xff & encryption[i]));
            }
        }

        return strBuf.toString();
    }

    public static String getUnique() {
        return getMd5(getImei());
    }

    public static String getImei() {
        String code = System.currentTimeMillis() + "1";
        int total = 0, sum1 = 0, sum2 = 0, temp = 0;
        char[] chs = code.toCharArray();
        for (int i = 0; i < chs.length; i++) {
            int num = chs[i] - '0';
            if (i % 2 == 0) {
                sum1 = sum1 + num;
            } else {
                temp = num * 2;
                if (temp < 10) {
                    sum2 = sum2 + temp;
                } else {
                    sum2 = sum2 + temp + 1 - 10;
                }
            }
        }
        total = sum1 + sum2;
        if (total % 10 == 0) {
            return "0";
        } else {
            return (10 - (total % 10)) + "";
        }
    }


    public static String getUuid() {
        return UUID.randomUUID().toString().replace("-", "");
    }

    public static void updatePayTime(long nowTime, String capitalDetailId) throws ClassNotFoundException, SQLException, InstantiationException, IllegalAccessException {
        Date currentTime = new Date(nowTime);
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String dateString = formatter.format(currentTime);
        Timestamp timestamp = new Timestamp(nowTime - 111605000L);
        String tableName = "capital_detail";
        String sql = "update " + tableName + " set pay_time = '" + timestamp + "' " +
                "where capital_detail_id = " + capitalDetailId;
        System.out.println(sql);
        Database.action(sql);
    }
}
