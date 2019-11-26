package xinniu.test.limit;

import com.alibaba.fastjson.JSONObject;
import com.aventstack.extentreports.ExtentTest;
import com.xinniu.init.TestBase;
import com.xinniu.util.PrintUtil;
import org.testng.ITestContext;
import org.testng.ITestNGMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.lang.reflect.Method;

/**
 * @Author: sunjinghai
 * @Date: 2019-09-03 10:23
 * @Version 1.0
 */
public class ExclusLimitTest extends TestBase {

    private ExtentTest assertTest;

    private String host = SCHEME+ HOST + SERVER;

    private String path = "/v1/limits/excluslimit";

    @BeforeMethod
    public void before(Method method, ITestContext iTestContext) {
        String caseDesc = null;
        PrintUtil.printC(method.getName());
        for (ITestNGMethod iTestNGMethod : iTestContext.getAllTestMethods()) {
            if (iTestNGMethod.getMethodName().equals(method.getName())) {
                caseDesc = iTestNGMethod.getDescription();
            }
        }
        if (caseDesc == null) {
            assertTest = extent.createTest("[专享额度]"+method.getName());
        } else {
            assertTest = extent.createTest("[专享额度]"+caseDesc);
        }
    }

    @Test(description = "获取公积金专享额度列表")
    public void test1(){
        JSONObject body = new JSONObject();
        body.put("cat","fund");
        JSONObject result = doGetRequest(HOST+SERVER,path,body);
        PrintUtil.printC(result);
    }
}
