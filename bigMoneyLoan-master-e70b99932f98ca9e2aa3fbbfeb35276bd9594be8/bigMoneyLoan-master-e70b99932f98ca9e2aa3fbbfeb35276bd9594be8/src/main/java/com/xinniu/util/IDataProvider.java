package com.xinniu.util;

import java.io.File;
import java.lang.reflect.Method;
import java.util.Iterator;

import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * @author sunjinghai
 */
public class IDataProvider {

    static Iterator<Object[]> data;

//    static String DATA_DIRECTORY = "testdata/";
    static String DATA_DIRECTORY = "";

    static final String CSV_FILE_POSTFIX = ".csv";

    static final String SEPARATOR_NONE = "none";//类名_方法名
    static final String SEPARATOR_CLASS_NAME = "class";//类名/方法名
    static final String SEPARATOR_PACKAGE_NAME = "package";//包名（最后一位）／类名_方法名

    static Iterator<Object[]> loadFile(File file) {
        return data;
    }

    static boolean validFile(File file) {
        return file != null && file.exists() && !file.isDirectory() && file.canRead();
    }

    static File getFile(Method method, String postFix) {
        return getFileD(method, postFix, SEPARATOR_PACKAGE_NAME);
    }

    static File getFileD(Method method, String postFix, String separator) {
        if (method == null || StringUtils.isBlank(postFix) || StringUtils.isBlank(separator)) {
            return null;
        }

        String clsName = method.getDeclaringClass().getSimpleName();
        String[] canonicalName = StringUtils.split(method.getDeclaringClass().getCanonicalName(), ".");
        String mtdName = method.getName();
        String fileDir;
        String path = IDataProvider.class.getResource("/").getPath();
        PrintUtil.printB("path文件路径：" + path);

        switch (separator) {
            case SEPARATOR_NONE:
                fileDir = path + DATA_DIRECTORY + clsName + "_" + mtdName + postFix;
                break;
            case SEPARATOR_CLASS_NAME:
                fileDir = path + DATA_DIRECTORY + clsName + "/" + mtdName + postFix;
                break;
            case SEPARATOR_PACKAGE_NAME:
                //取包名的最后一位
                fileDir = path + DATA_DIRECTORY + canonicalName[canonicalName.length - 2] + "/" + clsName
                    + "_" + mtdName + postFix;
                break;
            default:
                fileDir = path + DATA_DIRECTORY + clsName + "/" + mtdName + postFix;
                break;
        }
        PrintUtil.printB("文件路径：" + fileDir);

        return new File(fileDir);
    }
}
