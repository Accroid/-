package com.xinniu.extent;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

/**
 * Created by sunjinghai on 2018/12/6.
 */
public class ExtentTestNGITestListener implements ITestListener {

    private static ExtentReports extent = ExtentManager.createInstance("extent.html");
    //private static ThreadLocal parentTest = new ThreadLocal();
    //private static ThreadLocal test = new ThreadLocal();
    //不造为嘛，代码苦手表示用上面的代码就是编译报错，所以就随便改了改，如下，就通过了。。
    private static ThreadLocal<ExtentTest> parentTest = new ThreadLocal();
    private static ThreadLocal<ExtentTest> test = new ThreadLocal();

    @Override
    public synchronized void onStart(ITestContext context) {
        ExtentTest parent = extent.createTest(getClass().getName());
        parentTest.set(parent);
    }

    @Override
    public synchronized void onFinish(ITestContext context) {
        extent.flush();
    }

    @Override
    public synchronized void onTestStart(ITestResult result) {
        ExtentTest child = parentTest.get().createNode(result.getMethod().getMethodName());
        test.set(child);
    }

    @Override
    public synchronized void onTestSuccess(ITestResult result) {
        test.get().pass("Test passed");
    }

    @Override
    public synchronized void onTestFailure(ITestResult result) {
        test.get().fail(result.getThrowable());
    }

    @Override
    public synchronized void onTestSkipped(ITestResult result) {
        test.get().skip(result.getThrowable());
    }

    @Override
    public synchronized void onTestFailedButWithinSuccessPercentage(ITestResult result) {

    }
}
