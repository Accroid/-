package com.xinniu.common;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

/**
 * Created by sunjinghai on 2018/7/20.
 */
public class ClearRedis {
    public static void main(String[] args) {
        List<String> tempList = Arrays.asList(redisData);

        JedisPool jedisPool = new JedisPool("115.231.223.139", 9904);
        Jedis jedis = null;
        try {
            jedis = jedisPool.getResource();
            String pre_str = "otc_user_trade_cancle_";
            Set<String> set = jedis.keys(pre_str + "*");
            Iterator<String> it = set.iterator();
            while (it.hasNext()) {
                String keyStr = it.next();
                System.out.println(keyStr);
                if (tempList.contains(keyStr)){
                    jedis.del(keyStr);
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (jedis != null)
                jedis.close();
        }
        jedisPool.destroy();

    }

    private static String[] redisData = {
            "otc_user_trade_cancle_17918",
            "otc_user_trade_cancle_17919",
            "otc_user_trade_cancle_17920",
            "otc_user_trade_cancle_17921",
            "otc_user_trade_cancle_17922",
            "otc_user_trade_cancle_17923",
            "otc_user_trade_cancle_17924",
            "otc_user_trade_cancle_17925",
            "otc_user_trade_cancle_17926",
            "otc_user_trade_cancle_17888",
            "otc_user_trade_cancle_17927"};
}
