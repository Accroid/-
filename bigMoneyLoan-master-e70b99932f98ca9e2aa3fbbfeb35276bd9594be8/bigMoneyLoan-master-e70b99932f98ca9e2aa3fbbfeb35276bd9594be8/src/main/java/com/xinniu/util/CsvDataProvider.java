package com.xinniu.util;

import au.com.bytecode.opencsv.CSVReader;
import com.xinniu.util.IDataProvider;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.testng.ITestContext;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


/**
 * @author sunjinghai
 */
public class CsvDataProvider extends IDataProvider {

//    @DataProvider(name = "csv")
//    public static TestDataDTO provider(Method method, ITestContext context) {
//
//        File file = getFile(method, CSV_FILE_POSTFIX);
//        if (validFile(file)) {
//            return loadFile(file);
//        } else {
//            PrintUtil.printR("指定的文件不存在，或者不可读！");
//            return null;
//        }
//    }
//
//    protected static TestDataDTO loadFile(File file) {
//        CSVReader reader;
//        List<Object[]> list = new ArrayList<>();
//        try {
//            reader = new CSVReader(new FileReader(file), ',', '\"', 1);
//            String[] nextLine = reader.readNext();
//
//            while (nextLine != null) {
//                list.add(nextLine);
//                nextLine = reader.readNext();
//            }
//        } catch (FileNotFoundException e) {
//            e.printStackTrace();
//            PrintUtil.printR("参数文件有误！");
//            return null;
//        } catch (IOException e) {
//            e.printStackTrace();
//            PrintUtil.printR("读取文件出错！");
//            return null;
//        }
//        TestDataDTO testDataDTO = new TestDataDTO();
//        testDataDTO.setCaseId(list.get(0).toString());
//        testDataDTO.setCaseName(list.get(1).toString());
//        testDataDTO.setUrl(list.get(2).toString());
//        testDataDTO.setMethod(list.get(3).toString());
//        testDataDTO.setParams(list.get(4).toString());
//        testDataDTO.setBody(list.get(5).toString());
//        testDataDTO.setCode(list.get(6).toString());
//        testDataDTO.setMessage(list.get(7).toString());
//
//
//        return testDataDTO;
//    }

    @DataProvider(name = "csv")
    public static Iterator<Object[]> provider(Method method, ITestContext context) {

        File file = getFile(method, CSV_FILE_POSTFIX);
        if (validFile(file)) {
            return loadFile(file);
        } else {
            PrintUtil.printR("指定的文件不存在，或者不可读！");
            return null;
        }
    }

    protected static Iterator<Object[]> loadFile(File file) {
        CSVReader reader;
        List<Object[]> list = new ArrayList<>();
        List<Object> item = new ArrayList<Object>();

        try {
            reader = new CSVReader(new FileReader(file), ',', '\"', 1);
            String[] nextLine = reader.readNext();

            while (nextLine != null) {
                TestDataDTO testDataDTO = new TestDataDTO();
                testDataDTO.setCaseId(nextLine[0]);
                testDataDTO.setCaseName(nextLine[1]);
                testDataDTO.setUrl(nextLine[2]);
                testDataDTO.setMethod(nextLine[3]);
                testDataDTO.setParams(nextLine[4]);
                testDataDTO.setBody(nextLine[5]);
                testDataDTO.setClientType(nextLine[6]);
                testDataDTO.setCode(nextLine[7]);
                testDataDTO.setResult(nextLine[8]);
                try {
                    testDataDTO.setStatus(nextLine[11]);
                }catch (Exception e){
                    testDataDTO.setStatus("");
                }
                item.add(testDataDTO);
//                PrintUtil.printM("sjh=" + testDataDTO);
                nextLine = reader.readNext();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            PrintUtil.printR("参数文件有误！");
            return null;
        } catch (IOException e) {
            e.printStackTrace();
            PrintUtil.printR("读取文件出错！");
            return null;
        }


        for (Object u : item) {
            //做一个形式转换
            list.add(new Object[]{u});
        }

        return list.iterator();
    }


}
