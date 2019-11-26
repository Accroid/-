package com.xinniu.init;

import com.alibaba.fastjson.JSONObject;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ResourceCDN;
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import com.aventstack.extentreports.reporter.configuration.ChartLocation;
import com.google.common.collect.Multimap;
import com.xinniu.util.PrintUtil;
import okhttp3.Response;
import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeSuite;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;
import redis.clients.jedis.JedisSentinelPool;

import java.text.SimpleDateFormat;
import java.util.*;


/**
 * Created by sunjinghai on 2018/6/8.
 */
@Component
@Configuration
@PropertySource(value = "classpath:environmentInit.properties")
@ContextConfiguration("classpath:/spring.xml")
public class TestBase extends AbstractTestNGSpringContextTests {
    protected final Logger logger = LoggerFactory.getLogger(getClass());

    @Value("${scheme}")
    protected String SCHEME;

    @Value("${host}")
    protected String HOST;

    @Value("${server}")
    protected String SERVER;



    @Autowired
    private HttpService httpService;

    protected static ExtentReports extent;
    protected static ExtentHtmlReporter htmlReporter;



    @BeforeSuite
    public void befores() {
        extent = new ExtentReports();
        htmlReporter = new ExtentHtmlReporter("extent.html");
        extent.attachReporter(htmlReporter);
        htmlReporter.config().setDocumentTitle("大额贷测试报告");
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String time = format.format(Calendar.getInstance().getTime());
        htmlReporter.config().setReportName("大额贷测试报告 [" + time + "]");
        htmlReporter.config().setTestViewChartLocation(ChartLocation.TOP);
    }

    @BeforeClass
    public void setUp(){
        PrintUtil.printC("初始化连接数据");
        PrintUtil.printC(HOST);
    }

    @AfterSuite
    public void afters() {
        htmlReporter.config().setResourceCDN(ResourceCDN.EXTENTREPORTS);
        extent.setReportUsesManualConfiguration(true);
        extent.flush();
    }

    protected String doGetRequest(String host, String path) {
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doGet(HTTPURL + path);
        String responseBody2String = httpService.parseResponseBody2String(result);
        return responseBody2String;
    }

    protected JSONObject doGetRequest(String host, String path, Multimap<String, String> headers) {
        PrintUtil.printB(headers);
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doGet(HTTPURL + path, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doGetRequest(String host, String path, String body, Multimap<String, String> headers) {
        PrintUtil.printB(headers);
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doGet(HTTPURL + path, body, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doGetRequest(String host, String path, Map<String, Object> body, Multimap<String, String> headers) {
        PrintUtil.printB(headers);
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doGet(HTTPURL + path, body, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doGetRequest(String host, String path, Map<String, Object> body) {
        PrintUtil.printC(body.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doGet(HTTPURL + path, body);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPostRequest(String host, String path, Multimap<String, String> headers) {
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPost(HTTPURL + path, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPostRequest(String host, String path, Map<String, Object> param) {
        PrintUtil.printC(param.toString());
        String HTTPURL = SCHEME + "://" + host;
//        String url = "?";
//        for (String key : param.keySet()) {
//            url = url + key + "=" + param.get(key) + "&";
//        }
//        url = url.substring(0, url.length() - 1);
        Response result = httpService.doPost(HTTPURL + path ,param);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        PrintUtil.printC(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPutRequest(String host, String path, Multimap<String, String> headers) {
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPut(HTTPURL + path, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
//        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doDeleteRequest(String host, String path, Multimap<String, String> headers) {
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doDelete(HTTPURL + path, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
//        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPostRequest(String host, String path, String body) {
        PrintUtil.printB(body);
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPost(HTTPURL + path, body);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
//        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPostRequest(String host, String path, String body, Multimap<String, String> headers) {
        PrintUtil.printB(body);
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPost(HTTPURL + path, body, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
//        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doPutRequest(String host, String path, String body, Multimap<String, String> headers) {
        PrintUtil.printB(body);
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPut(HTTPURL + path, body, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

    protected JSONObject doDeleteRequest(String host, String path, String body, Multimap<String, String> headers) {
        PrintUtil.printB(body);
        PrintUtil.printB(headers.toString());
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doDelete(HTTPURL + path, body, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        logger.info(jsonObject.toJSONString());

        return jsonObject;
    }

//    protected JSONObject doPostRequest(String host, String path, Multimap<String, String> body) {
//        String HTTPURL = SCHEME + "://" + host + ":" + PORT;
//        Response result = httpService.doPost(HTTPURL + path, JSONObject.toJSONString(body));
//        String responseBody2String = httpService.parseResponseBody2String(result);
//        logger.info(responseBody2String);
//        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
//        logger.info(jsonObject.toJSONString());
//
//        return jsonObject;
//    }

    protected JSONObject doPostRequest(String host, String path, Map<String, Object> param, Multimap<String, String> headers) {
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPost(HTTPURL + path, param, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        logger.info(responseBody2String);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        logger.info(jsonObject.toJSONString());
        return jsonObject;
    }

    protected JSONObject doPutRequest(String host, String path, Map<String, Object> param, Multimap<String, String> headers) {
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doPut(HTTPURL + path, param, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        logger.info(responseBody2String);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        logger.info(jsonObject.toJSONString());
        return jsonObject;
    }

    protected JSONObject doDeleteRequest(String host, String path, Map<String, Object> param, Multimap<String, String> headers) {
        String HTTPURL = SCHEME + "://" + host;
        Response result = httpService.doDelete(HTTPURL + path, param, headers);
        String responseBody2String = httpService.parseResponseBody2String(result);
        logger.info(responseBody2String);
        JSONObject jsonObject = JSONObject.parseObject(responseBody2String);
        logger.info(jsonObject.toJSONString());
        return jsonObject;
    }

    //type=0为商户端,type=1为采购端,type=2信牛管理端
    protected String getImageCode(int type) {
        String clientType=null;
        switch (type){
            case 0:
                clientType = "server";
                break;
            case 1:
                clientType = "goods";
                break;
            case 2:
                clientType = "admin";
                break;
        }
        JedisPoolConfig jedisPoolConfig = new JedisPoolConfig();

        Set<String> sentinels = new HashSet<>(Arrays.asList(
                "192.168.0.57:27070",
                "192.168.1.52:27070",
                "192.168.1.55:27070"
        ));
        jedisPoolConfig.setMaxIdle(10);
        jedisPoolConfig.setMaxTotal(200);
        jedisPoolConfig.setMaxWaitMillis(1000 * 10);
        jedisPoolConfig.setTestOnBorrow(true);

//        GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig();
//        poolConfig.setMaxTotal(10);
//        poolConfig.setMaxIdle(5);
//        poolConfig.setMinIdle(5);
        JedisSentinelPool jedisPool = new JedisSentinelPool("loan", sentinels, jedisPoolConfig,"Xinniu_redis-1@2017");
//        JedisPool jedisPool = new JedisPool(poolConfig, "192.168.0.57", 27070, 10000, "Xinniu_redis-1@2017");
        Jedis jedis = null;
        String code = null;
        try {
            jedis = jedisPool.getResource();
            PrintUtil.printC(jedis);
            String pre_str = "imageCode";
            Set<String> set = jedis.keys(pre_str + "*");
            Iterator<String> it = set.iterator();
            while (it.hasNext()) {
                String keyStr = it.next();
                System.out.println(keyStr);
                PrintUtil.printC(jedis.get(keyStr));
                code = jedis.get(keyStr);
                code = code.substring(code.length()-4);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (jedis != null) {
                jedis.close();
                return code;
            }
        }
        jedisPool.destroy();
        return code;
    }


    protected String getDrawCodeFromRedis(String deviceId) {
        GenericObjectPoolConfig poolConfig = new GenericObjectPoolConfig();

        JedisPool jedisPool = new JedisPool(poolConfig, "192.168.4.117", 6379, 10000, "qwerty");
        Jedis jedis = null;
        String code = null;
        try {

            jedis = jedisPool.getResource();
            String pre_str = "verifycode:" + deviceId;
            Set<String> set = jedis.keys(pre_str + "*");
            Iterator<String> it = set.iterator();
            while (it.hasNext()) {
                String keyStr = it.next();
                System.out.println(keyStr);
                PrintUtil.printC(jedis.get(keyStr));
                code = jedis.get(keyStr);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (jedis != null) {
                jedis.close();
                return code;
            }
        }
        jedisPool.destroy();
        return code;
    }
}
