//package com.mpm.extent;
//
//import com.aventstack.extentreports.ExtentReports;
//import com.aventstack.extentreports.ExtentTest;
//import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
//import org.testng.ITestResult;
//import org.testng.annotations.AfterMethod;
//import org.testng.annotations.BeforeClass;
//import org.testng.annotations.BeforeMethod;
//import org.testng.annotations.BeforeSuite;
//
//import java.lang.reflect.Method;
//
///**
// * Created by sunjinghai on 2018/12/6.
// */
//public class ExtentTestNGReportBuilder {
//    private static ExtentReports extent;
//    private static ThreadLocal parentTest = new ThreadLocal();
//    private static ThreadLocal test = new ThreadLocal();
//
//    @BeforeSuite
//    public void beforeSuite() {
//        extent = ExtentManager.createInstance("extent.html");
//        ExtentHtmlReporter htmlReporter = new ExtentHtmlReporter("extent.html");
//        extent.attachReporter(htmlReporter);
//    }
//
//    @BeforeClass
//    public synchronized void beforeClass() {
//        ExtentTest parent = extent.createTest(getClass().getName());
//        parentTest.set(parent);
//    }
//
//    @BeforeMethod
//    public synchronized void beforeMethod(Method method) {
//        ExtentTest child = parentTest.get().createNode(method.getName());
//        test.set(child);
//    }
//
//    @AfterMethod
//    public synchronized void afterMethod(ITestResult result) {
//        if (result.getStatus() == ITestResult.FAILURE) {
//            test.get().fail(result.getThrowable());
//        } else if (result.getStatus() == ITestResult.SKIP) {
//            test.get().skip(result.getThrowable());
//        } else {
//            test.get().pass("Test passed");
//        }
//
//        extent.flush();
//    }
//}
