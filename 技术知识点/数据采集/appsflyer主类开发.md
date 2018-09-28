## appsflyer pom源
```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.appsflyerlog</groupId>
	<artifactId>appsflyerlog</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>jar</packaging>

	<name>appsflyerlog</name>
	<url>http://maven.apache.org</url>
	
	<properties>
		<!-- Set default encoding to UTF-8 to remove maven complaints -->
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<!-- Java compiler configuration -->
		<sourceJavaVersion>1.7</sourceJavaVersion>
		<targetJavaVersion>1.7</targetJavaVersion>
		<slf4j.version>1.7.12</slf4j.version>
		<logback.version>1.0.1</logback.version>
	</properties>
	<dependencies>
		<dependency>
			<groupId>io.netty</groupId>
			<artifactId>netty-all</artifactId>
			<version>5.0.0.Alpha1</version>
		</dependency>
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>javax.servlet-api</artifactId>
			<version>3.1.0</version>
			<scope>provided</scope>
		</dependency>
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>fastjson</artifactId>
			<version>1.2.7</version>
		</dependency>
		
		
			<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>${logback.version}</version>
		</dependency>
		<dependency>

			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
			<version>${logback.version}</version>
		</dependency>
		
		
			<dependency>
			<groupId>log4j</groupId>
			<artifactId>log4j</artifactId>
			<version>1.2.17</version>
			<exclusions>
				<exclusion>
					<groupId>com.sun.jdmk</groupId>
					<artifactId>jmxtools</artifactId>
				</exclusion>
				<exclusion>
					<groupId>com.sun.jmx</groupId>
					<artifactId>jmxri</artifactId>
				</exclusion>
			</exclusions>
		</dependency>

		<dependency>
			<groupId>log4j</groupId>
			<artifactId>apache-log4j-extras</artifactId>
			<version>1.1</version>
		</dependency>

		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-api</artifactId>
			<version>${slf4j.version}</version>
		</dependency>


		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>slf4j-log4j12</artifactId>
			<version>${slf4j.version}</version>
		</dependency>
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>3.8.1</version>
			<scope>test</scope>
		</dependency>
	</dependencies>
	
		<build>
		<finalName>appsflyerlog</finalName>

		<plugins>
			<!-- MAVEN 编译使用的JDK版本 -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>2.3.2</version>
				<configuration>
					<source>${sourceJavaVersion}</source>
					<target>${targetJavaVersion}</target>
					<encoding>UTF-8</encoding>
				</configuration>
				<dependencies>
					<dependency>
						<groupId>org.codehaus.plexus</groupId>
						<artifactId>plexus-compiler-javac</artifactId>
						<version>1.8.1</version>
					</dependency>
				</dependencies>
			</plugin>


			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-jar-plugin</artifactId>
				<configuration>
					<archive>
						<manifest>
							<addClasspath>true</addClasspath>
						</manifest>
					</archive>
				</configuration>
			</plugin>
			
   <plugin>
      <artifactId>maven-assembly-plugin</artifactId>
      <configuration>
        <archive>
          <manifest>
            <mainClass>fully.qualified.MainClass</mainClass>
          </manifest>
        </archive>
        <descriptorRefs>
          <descriptorRef>jar-with-dependencies</descriptorRef>
        </descriptorRefs>
      </configuration>
    </plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-resources-plugin</artifactId>
				<version>2.4.1</version>
				<configuration>
					<encoding>UTF-8</encoding>
				</configuration>
			</plugin>
			<!-- 可以跳过测试，当测试失败仍然执行 -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<configuration>
					<skip>true</skip>
				</configuration>
			</plugin>

<!-- 			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-war-plugin</artifactId>
				<version>2.1</version>
				<configuration>
					<warName>test</warName>
				</configuration>
			</plugin> -->

            <!-- jetty -->

			<!-- 
			<plugin>
				http://wiki.eclipse.org/Jetty/Feature/Jetty_Maven_Plugin
				<groupId>org.mortbay.jetty</groupId>
				<artifactId>jetty-maven-plugin</artifactId>
				<version>8.0.0.M3</version>
				<configuration>
					<stopPort>9966</stopPort>
					<stopKey>foo</stopKey>
					<scanIntervalSeconds>0</scanIntervalSeconds>
					<connectors>
						<connector implementation="org.eclipse.jetty.server.nio.SelectChannelConnector">
							<port>8088</port>
							<maxIdleTime>60000</maxIdleTime>
						</connector>
					</connectors>
					<webAppConfig>
						<contextPath>/test</contextPath>
					</webAppConfig>
				</configuration>
			</plugin> -->
		</plugins>
	</build>
</project>

```

## main
### model
* AppExtendTags
```
package com.appsflyerlog.model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import com.fastjson.JSON;
import com.appsflyerlog.util.Constant;

public class AppExtendTags implements Serializable {

	private static final long serialVersionUID = 1615072541143990300L;
	private String appsFlyerId ;
	private String af_date_a ;
	private String af_customer_user_id ;
	private String af_content_type ;
	private String af_search_string ;
	private String itemcode ;
	private String cid ;
	private String oidList ;
	private String cartIds ;
	private String af_revenue ;
	public String getAppsFlyerId() {
		return appsFlyerId;
	}
	public void setAppsFlyerId(String appsFlyerId) {
		this.appsFlyerId = appsFlyerId;
	}
	public String getAf_date_a() {
		return af_date_a;
	}
	public void setAf_date_a(String af_date_a) {
		this.af_date_a = af_date_a;
	}
	public String getAf_customer_user_id() {
		return af_customer_user_id;
	}
	public void setAf_customer_user_id(String af_customer_user_id) {
		this.af_customer_user_id = af_customer_user_id;
	}
	public String getAf_content_type() {
		return af_content_type;
	}
	public void setAf_content_type(String af_content_type) {
		this.af_content_type = af_content_type;
	}
	public String getAf_search_string() {
		return af_search_string;
	}
	public void setAf_search_string(String af_search_string) {
		this.af_search_string = af_search_string;
	}
	public String getItemcode() {
		return itemcode;
	}
	public void setItemcode(String itemcode) {
		this.itemcode = itemcode;
	}
	public String getCid() {
		return cid;
	}
	public void setCid(String cid) {
		this.cid = cid;
	}
	public String getOidList() {
		return oidList;
	}
	public void setOidList(String oidList) {
		this.oidList = oidList;
	}
	public String getCartIds() {
		return cartIds;
	}
	public void setCartIds(String cartIds) {
		this.cartIds = cartIds;
	}
	public String getAf_revenue() {
		return af_revenue;
	}
	public void setAf_revenue(String af_revenue) {
		this.af_revenue = af_revenue;
	}
	@Override
	public String toString() {
		
		StringBuffer extendBuf = new StringBuffer();
		extendBuf.append(formatString(this.getAppsFlyerId())).append(Constant.L2);
		extendBuf.append(formatString(this.getAf_date_a())).append(Constant.L2);
		extendBuf.append(formatString(this.getAf_customer_user_id())).append(Constant.L2);
		extendBuf.append(formatString(this.getAf_content_type())).append(Constant.L2);
		extendBuf.append(formatString(this.getAf_search_string())).append(Constant.L2);
		extendBuf.append(formatString(this.getItemcode())).append(Constant.L2);
		extendBuf.append(formatString(this.getCid())).append(Constant.L2);
		extendBuf.append(formatString(this.getOidList())).append(Constant.L2);
		extendBuf.append(formatString(this.getCartIds())).append(Constant.L2);
		extendBuf.append(formatString(this.getAf_revenue()));
		return extendBuf.toString();
	}
	
	private String formatString(Object obj) {
		return obj == null ? "" : obj.toString().trim();
	}
	
	public static void main(String[] args){
		List<AppExtendTags> extag = JSON.parseArray(args[0],
				AppExtendTags.class);
		System.out.println(extag.toString());
	}
}

```
* AppsFlyerLog
```
package com.appsflyerlog.model;

import java.io.Serializable;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.List;

import com.fastjson.JSON;
import com.appsflyerlog.util.Constant;

public class AppsFlyerLog implements Serializable {
	
	private static final long serialVersionUID = -1025970403620362800L;
	
	  private String app_id               ;
	  private String platform             ;
	  private String click_time           ;
	  private String install_time         ;
	  private String agency               ;
	  private String media_source         ;
	  private String campaign             ;
	  private String fb_campaign_name     ;
	  private String fb_campaign_id       ;
	  private String fb_adset_name        ;
	  private String fb_adset_id          ;
	  private String fb_adgroup_name      ;
	  private String fb_adgroup_id        ;
	  private String af_siteid            ;
	  private String cost_per_install     ;
	  private String country_code         ;
	  private String city                 ;
	  private String ip                   ;
	  private String wifi                 ;
	  private String language             ;
	  private String appsflyer_device_id  ;
	  private String customer_user_id     ;
	  private String idfa                 ;
	  private String idfv                 ;
	  private String mac                  ;
	  private String device_name          ;
	  private String device_type          ;
	  private String os_version           ;
	  private String sdk_version          ;
	  private String app_version          ;
	  private String event_type           ;
	  private String event_name           ;
	  private String event_value          ;
	  private String currency             ;
	  private String event_time           ;
	  private String af_sub1              ;
	  private String af_sub2              ;
	  private String af_sub3              ;
	  private String af_sub4              ;
	  private String af_sub5              ;
	  private String click_url            ;
	  private String attribution_type     ;
	  private String http_referrer        ;	

	  private String operator       ;
	  private String advertising_id ;
	  private String android_id ;
	  private String imei ;

	  /*public AppsFlyerLog1(String app_id, String platform, String click_time,
			String install_time, String agency, String media_source,
			String campaign, String fb_campaign_name, String fb_campaign_id,
			String fb_adset_name, String fb_adset_id, String fb_adgroup_name,
			String fb_adgroup_id, String af_siteid, String cost_per_install,
			String country_code, String city, String ip, String wifi,
			String language, String appsflyer_device_id,
			String customer_user_id, String idfa, String idfv, String mac,
			String device_name, String device_type, String os_version,
			String sdk_version, String app_version, String event_type,
			String event_name, String event_value, String currency,
			String event_time, String af_sub1, String af_sub2, String af_sub3,
			String af_sub4, String af_sub5, String click_url,
			String attribution_type, String http_referrer, String operator,
			String advertising_id, String android_id, String imei) {
		this.app_id = app_id;
		this.platform = platform;
		this.click_time = click_time;
		this.install_time = install_time;
		this.agency = agency;
		this.media_source = media_source;
		this.campaign = campaign;
		this.fb_campaign_name = fb_campaign_name;
		this.fb_campaign_id = fb_campaign_id;
		this.fb_adset_name = fb_adset_name;
		this.fb_adset_id = fb_adset_id;
		this.fb_adgroup_name = fb_adgroup_name;
		this.fb_adgroup_id = fb_adgroup_id;
		this.af_siteid = af_siteid;
		this.cost_per_install = cost_per_install;
		this.country_code = country_code;
		this.city = city;
		this.ip = ip;
		this.wifi = wifi;
		this.language = language;
		this.appsflyer_device_id = appsflyer_device_id;
		this.customer_user_id = customer_user_id;
		this.idfa = idfa;
		this.idfv = idfv;
		this.mac = mac;
		this.device_name = device_name;
		this.device_type = device_type;
		this.os_version = os_version;
		this.sdk_version = sdk_version;
		this.app_version = app_version;
		this.event_type = event_type;
		this.event_name = event_name;
		this.event_value = event_value;
		this.currency = currency;
		this.event_time = event_time;
		this.af_sub1 = af_sub1;
		this.af_sub2 = af_sub2;
		this.af_sub3 = af_sub3;
		this.af_sub4 = af_sub4;
		this.af_sub5 = af_sub5;
		this.click_url = click_url;
		this.attribution_type = attribution_type;
		this.http_referrer = http_referrer;
		this.operator = operator;
		this.advertising_id = advertising_id;
		this.android_id = android_id;
		this.imei = imei;
	}	*/  
	public String getApp_id() {
		return app_id;
	}
	public void setApp_id(String app_id) {
		this.app_id = app_id;
	}
	public String getPlatform() {
		return platform;
	}
	public void setPlatform(String platform) {
		this.platform = platform;
	}
	public String getClick_time() {
		return click_time;
	}
	public void setClick_time(String click_time) {
		this.click_time = click_time;
	}
	public String getInstall_time() {
		return install_time;
	}
	public void setInstall_time(String install_time) {
		this.install_time = install_time;
	}
	public String getAgency() {
		return agency;
	}
	public void setAgency(String agency) {
		this.agency = agency;
	}
	public String getMedia_source() {
		return media_source;
	}
	public void setMedia_source(String media_source) {
		this.media_source = media_source;
	}
	public String getCampaign() {
		return campaign;
	}
	public void setCampaign(String campaign) {
		this.campaign = campaign;
	}
	public String getFb_campaign_name() {
		return fb_campaign_name;
	}
	public void setFb_campaign_name(String fb_campaign_name) {
		this.fb_campaign_name = fb_campaign_name;
	}
	public String getFb_campaign_id() {
		return fb_campaign_id;
	}
	public void setFb_campaign_id(String fb_campaign_id) {
		this.fb_campaign_id = fb_campaign_id;
	}
	public String getFb_adset_name() {
		return fb_adset_name;
	}
	public void setFb_adset_name(String fb_adset_name) {
		this.fb_adset_name = fb_adset_name;
	}
	public String getFb_adset_id() {
		return fb_adset_id;
	}
	public void setFb_adset_id(String fb_adset_id) {
		this.fb_adset_id = fb_adset_id;
	}
	public String getFb_adgroup_name() {
		return fb_adgroup_name;
	}
	public void setFb_adgroup_name(String fb_adgroup_name) {
		this.fb_adgroup_name = fb_adgroup_name;
	}
	public String getFb_adgroup_id() {
		return fb_adgroup_id;
	}
	public void setFb_adgroup_id(String fb_adgroup_id) {
		this.fb_adgroup_id = fb_adgroup_id;
	}
	public String getAf_siteid() {
		return af_siteid;
	}
	public void setAf_siteid(String af_siteid) {
		this.af_siteid = af_siteid;
	}
	public String getCost_per_install() {
		return cost_per_install;
	}
	public void setCost_per_install(String cost_per_install) {
		this.cost_per_install = cost_per_install;
	}
	public String getCountry_code() {
		return country_code;
	}
	public void setCountry_code(String country_code) {
		this.country_code = country_code;
	}
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public String getIp() {
		return ip;
	}
	public void setIp(String ip) {
		this.ip = ip;
	}
	public String getWifi() {
		return wifi;
	}
	public void setWifi(String wifi) {
		this.wifi = wifi;
	}
	public String getLanguage() {
		return language;
	}
	public void setLanguage(String language) {
		this.language = language;
	}
	public String getAppsflyer_device_id() {
		return appsflyer_device_id;
	}
	public void setAppsflyer_device_id(String appsflyer_device_id) {
		this.appsflyer_device_id = appsflyer_device_id;
	}
	public String getCustomer_user_id() {
		return customer_user_id;
	}
	public void setCustomer_user_id(String customer_user_id) {
		this.customer_user_id = customer_user_id;
	}
	public String getIdfa() {
		return idfa;
	}
	public void setIdfa(String idfa) {
		this.idfa = idfa;
	}
	public String getIdfv() {
		return idfv;
	}
	public void setIdfv(String idfv) {
		this.idfv = idfv;
	}
	public String getMac() {
		return mac;
	}
	public void setMac(String mac) {
		this.mac = mac;
	}
	public String getDevice_name() {
		return device_name;
	}
	public void setDevice_name(String device_name) {
		this.device_name = device_name;
	}
	public String getDevice_type() {
		return device_type;
	}
	public void setDevice_type(String device_type) {
		this.device_type = device_type;
	}
	public String getOs_version() {
		return os_version;
	}
	public void setOs_version(String os_version) {
		this.os_version = os_version;
	}
	public String getSdk_version() {
		return sdk_version;
	}
	public void setSdk_version(String sdk_version) {
		this.sdk_version = sdk_version;
	}
	public String getApp_version() {
		return app_version;
	}
	public void setApp_version(String app_version) {
		this.app_version = app_version;
	}
	public String getEvent_type() {
		return event_type;
	}
	public void setEvent_type(String event_type) {
		this.event_type = event_type;
	}
	public String getEvent_name() {
		return event_name;
	}
	public void setEvent_name(String event_name) {
		this.event_name = event_name;
	}
	public String getEvent_value() {
		return event_value;
	}
	public void setEvent_value(String event_value) {
		this.event_value = event_value;
	}
	public String getCurrency() {
		return currency;
	}
	public void setCurrency(String currency) {
		this.currency = currency;
	}
	public String getEvent_time() {
		return event_time;
	}
	public void setEvent_time(String event_time) {
		this.event_time = event_time;
	}
	public String getAf_sub1() {
		return af_sub1;
	}
	public void setAf_sub1(String af_sub1) {
		this.af_sub1 = af_sub1;
	}
	public String getAf_sub2() {
		return af_sub2;
	}
	public void setAf_sub2(String af_sub2) {
		this.af_sub2 = af_sub2;
	}
	public String getAf_sub3() {
		return af_sub3;
	}
	public void setAf_sub3(String af_sub3) {
		this.af_sub3 = af_sub3;
	}
	public String getAf_sub4() {
		return af_sub4;
	}
	public void setAf_sub4(String af_sub4) {
		this.af_sub4 = af_sub4;
	}
	public String getAf_sub5() {
		return af_sub5;
	}
	public void setAf_sub5(String af_sub5) {
		this.af_sub5 = af_sub5;
	}
	public String getClick_url() {
		return click_url;
	}
	public void setClick_url(String click_url) {
		this.click_url = click_url;
	}
	public String getAttribution_type() {
		return attribution_type;
	}
	public void setAttribution_type(String attribution_type) {
		this.attribution_type = attribution_type;
	}
	public String getHttp_referrer() {
		return http_referrer;
	}
	public void setHttp_referrer(String http_referrer) {
		this.http_referrer = http_referrer;
	}
	  public String getOperator() {
		return operator;
	}
	public void setOperator(String operator) {
		this.operator = operator;
	}
	public String getAdvertising_id() {
		return advertising_id;
	}
	public void setAdvertising_id(String advertising_id) {
		this.advertising_id = advertising_id;
	}
	public String getAndroid_id() {
		return android_id;
	}
	public void setAndroid_id(String android_id) {
		this.android_id = android_id;
	}
	public String getImei() {
		return imei;
	}
	public void setImei(String imei) {
		this.imei = imei;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		AppsFlyerLog other = (AppsFlyerLog) obj;
		return other.app_id == this.app_id;
	}
	@Override
	public String toString() {
		StringBuffer publicBuf = new StringBuffer();
		publicBuf.append(formatString(this.getApp_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getPlatform())).append(Constant.L2);
		publicBuf.append(formatString(this.getClick_time())).append(Constant.L2);
		publicBuf.append(formatString(this.getInstall_time())).append(Constant.L2);
		publicBuf.append(formatString(this.getAgency())).append(Constant.L2);
		publicBuf.append(formatString(this.getMedia_source())).append(Constant.L2);
		publicBuf.append(formatString(this.getCampaign())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_campaign_name())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_campaign_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_adset_name())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_adset_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_adgroup_name())).append(Constant.L2);
		publicBuf.append(formatString(this.getFb_adgroup_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_siteid())).append(Constant.L2);
		publicBuf.append(formatString(this.getCost_per_install())).append(Constant.L2);
		publicBuf.append(formatString(this.getCountry_code())).append(Constant.L2);
		publicBuf.append(formatString(this.getCity())).append(Constant.L2);
		publicBuf.append(formatString(this.getIp())).append(Constant.L2);
		publicBuf.append(formatString(this.getWifi())).append(Constant.L2);
		publicBuf.append(formatString(this.getLanguage())).append(Constant.L2);
		publicBuf.append(formatString(this.getAppsflyer_device_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getCustomer_user_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getIdfa())).append(Constant.L2);
		publicBuf.append(formatString(this.getIdfv())).append(Constant.L2);
		publicBuf.append(formatString(this.getMac())).append(Constant.L2);
		publicBuf.append(formatString(this.getDevice_name())).append(Constant.L2);
		publicBuf.append(formatString(this.getDevice_type())).append(Constant.L2);
		publicBuf.append(formatString(this.getOs_version())).append(Constant.L2);
		publicBuf.append(formatString(this.getSdk_version())).append(Constant.L2);
		publicBuf.append(formatString(this.getApp_version())).append(Constant.L2);
		publicBuf.append(formatString(this.getEvent_type())).append(Constant.L2);
		publicBuf.append(formatString(this.getEvent_name())).append(Constant.L2);
		//publicBuf.append(formatString(this.getEvent_value())).append(Constant.L2);
		publicBuf.append(formatString(this.getCurrency())).append(Constant.L2);
		publicBuf.append(formatString(this.getEvent_time())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_sub1())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_sub2())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_sub3())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_sub4())).append(Constant.L2);
		publicBuf.append(formatString(this.getAf_sub5())).append(Constant.L2);
		publicBuf.append(formatString(this.getClick_url())).append(Constant.L2);
		publicBuf.append(formatString(this.getAttribution_type())).append(Constant.L2);
		publicBuf.append(formatString(this.getHttp_referrer())).append(Constant.L2);
		publicBuf.append(formatString(this.getOperator())).append(Constant.L2);
		publicBuf.append(formatString(this.getAdvertising_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getAndroid_id())).append(Constant.L2);
		publicBuf.append(formatString(this.getImei()));
		
		//System.out.println("extended tags: "+formatString(this.getEvent_value()));
		
		StringBuffer extendBuf = new StringBuffer();
		extendBuf.append("[");
		if(this.getEvent_value()!=null && !"".equals(this.getEvent_value())){	
			extendBuf.append(formatString(this.getEvent_value()));		
		} else {
			extendBuf.append("{\"appsFlyerId\":null,\"af_date_a\":null,\"af_content_type\":null}");	
		}	
		extendBuf.append("]");
		List<AppExtendTags> appExtendTags = null;
		appExtendTags=JSON.parseArray(extendBuf.toString(),AppExtendTags.class);
		
		String hostname=null;
		try {
			hostname=InetAddress.getLocalHost().getHostName();
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//System.out.println("extended tags: "+appExtendTags.toString().substring(1,appExtendTags.toString().length()-1));
		//System.out.println(publicBuf+Constant.L2+hostname+Constant.L2+appExtendTags.get(0));
		
		return publicBuf+Constant.L2+appExtendTags.get(0).toString()+Constant.L2+hostname;
	}
	private String formatString(Object obj) {
		return obj == null ? "" : obj.toString().trim();
	}
	
	public static void main(String[] args) {
		List<String> l1 = Arrays.asList("sup1", "sup2", "sup3");
		System.out.println(l1);
		
	}
}

```
### service
```
package com.appsflyerlog.service.impl;


import java.io.IOException;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.appsflyerlog.service.LoggingService;

/**
 * 写日志文件的服务类
 */
public class LoggingServiceImpl implements LoggingService {
    static Logger runLogger = LoggerFactory.getLogger(LoggingServiceImpl.class);
    static Logger appsFlyerLogger = LoggerFactory.getLogger("appsFlyerLog");
	public void saveLog(String app_id, String platform, String click_time,
			String install_time, String agency, String media_source,
			String campaign, String fb_campaign_name, String fb_campaign_id,
			String fb_adset_name, String fb_adset_id, String fb_adgroup_name,
			String fb_adgroup_id, String af_siteid, String cost_per_install,
			String country_code, String city, String ip, String wifi,
			String language, String appsflyer_device_id,
			String customer_user_id, String idfa, String idfv, String mac,
			String device_name, String device_type, String os_version,
			String sdk_version, String app_version, String event_type,
			String event_name, String event_value, String currency,
			String event_time, String af_sub1, String af_sub2, String af_sub3,
			String af_sub4, String af_sub5, String click_url,
			String attribution_type, String http_referrer, String operator,
			String advertising_id, String android_id, String imei) {
        //binLogger.info("aaa");
    }
   

	public void saveLog(String str) {
		// TODO Auto-generated method stub
		appsFlyerLogger.info(str);
	}

	


    
}
dh
```
### util
* app
```
package com.appsflyerlog;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}

```
* HttpServer
```
package com.appsflyerlog;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpRequestDecoder;
import io.netty.handler.codec.http.HttpResponseEncoder;
import io.netty.handler.codec.http.HttpServerCodec;
import io.netty.handler.stream.ChunkedWriteHandler;

public class HttpServer {

	public void run(final int port) throws Exception {
		EventLoopGroup bossGroup = new NioEventLoopGroup();
		EventLoopGroup workerGroup = new NioEventLoopGroup();
		try {
			ServerBootstrap b = new ServerBootstrap();
			b.group(bossGroup, workerGroup)
					.channel(NioServerSocketChannel.class)
					.childHandler(new ChannelInitializer<SocketChannel>() {
						@Override
						protected void initChannel(SocketChannel ch)
								throws Exception {
							// http解码支持-请求消息解码器
							ch.pipeline().addLast("http-decoder",
									new HttpRequestDecoder());
							// ch.pipeline().addLast("http-codec",new
							// HttpServerCodec());
							// 将多个消息转换为单一的request或者response对象
							ch.pipeline().addLast("http-aggregator",
									new HttpObjectAggregator(1000048576));
							// http编码支持-响应解码器
							ch.pipeline().addLast("http-encoder",
									new HttpResponseEncoder());
							// 业务逻辑
							ch.pipeline().addLast("httpServerHandler",
									new HttpServerHandler());
						}
					});

			ChannelFuture f = b.bind(port).sync();
			f.channel().closeFuture().sync();

		} finally {
			bossGroup.shutdownGracefully();
			workerGroup.shutdownGracefully();
		}
	}

	public static void main(String[] args) throws Exception {
		int port = 7001;
		
		/*
		 * if (args.length > 0) { try { port = Integer.parseInt(args[0]); }
		 * catch (NumberFormatException e) { e.printStackTrace(); } }
		 */

		new HttpServer().run(port);
	}
}
```

* HttpServerHandler
```
package com.mmmm.appsflyerlog;

import java.util.List;

import org.slf4j.LoggerFactory;
import org.slf4j.Logger;

import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.codec.http.DefaultFullHttpResponse;
import io.netty.handler.codec.http.FullHttpResponse;
import io.netty.handler.codec.http.HttpContent;
import io.netty.handler.codec.http.HttpMethod;
import io.netty.handler.codec.http.HttpRequest;
import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;
import io.netty.util.CharsetUtil;

import com.alibaba.fastjson.JSON;
import com.mmmm.appsflyerlog.model.AppsFlyerLog;
import com.mmmm.appsflyerlog.service.LoggingService;
import com.mmmm.appsflyerlog.service.impl.LoggingServiceImpl;

public class HttpServerHandler extends SimpleChannelInboundHandler<Object> {
	private Logger runLogger = LoggerFactory
			.getLogger(LoggingServiceImpl.class);
	private final StringBuilder buf = new StringBuilder();
	private HttpRequest request;

	@Override
	public void messageReceived(ChannelHandlerContext ctx, Object msg)
			throws Exception {

		HttpRequest request = this.request = (HttpRequest) msg;
//		System.out.println("---uri---" + request.getUri());
		if (msg instanceof HttpContent) {
			HttpContent httpContent = (HttpContent) msg;

			ByteBuf content = httpContent.content();
			if (content.isReadable()) {
				// buf.append("CONTENT: ");
				buf.append("[");
				buf.append(content.toString(CharsetUtil.UTF_8).replaceAll("\\n", " ").replaceAll("\\r", " ").replaceAll("\\007", ""));
				buf.append("]");
			}
		}
//		System.out.println("-1-----buf content----------" + buf.toString());
//		System.out.println("------");
//		System.out.println("-2-----request----------" + request.getMethod());
//		System.out.println("------");

		if (request.getMethod().equals(HttpMethod.POST)) {
			List<AppsFlyerLog> appsFlyerLog;
			try {
				appsFlyerLog = null;
				appsFlyerLog = JSON.parseArray(buf.toString(),
						AppsFlyerLog.class);
				LoggingService log = new LoggingServiceImpl();
				log.saveLog(appsFlyerLog.get(0).toString());
				//System.out.println("-3-----" + appsFlyerLog.get(0).toString());
				runLogger.info("accepted message from appsflyer");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				runLogger.error(e.getMessage());
				e.printStackTrace();
			}

		}
		FullHttpResponse response = new DefaultFullHttpResponse(
				HttpVersion.HTTP_1_1, HttpResponseStatus.OK);
		response.headers().set("Content-Type", "image/gif; charset=UTF-8");
		response.content().writeBytes("ok".getBytes());
		ctx.writeAndFlush(response).addListener(ChannelFutureListener.CLOSE);
	}

}
```
