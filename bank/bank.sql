/*
 Navicat Premium Data Transfer

 Source Server         : zywzyx
 Source Server Type    : MySQL
 Source Server Version : 50624
 Source Host           : localhost:3306
 Source Schema         : bank

 Target Server Type    : MySQL
 Target Server Version : 50624
 File Encoding         : 65001

 Date: 19/08/2021 17:19:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for abc
-- ----------------------------
DROP TABLE IF EXISTS `abc`;
CREATE TABLE `abc`  (
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '账号',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `country` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '国家',
  `province` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省份',
  `street` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '街道',
  `house` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '门牌号',
  `money` float(255, 2) NULL DEFAULT NULL COMMENT '余额',
  `bank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '开户行',
  `user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '账户等级'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of abc
-- ----------------------------
INSERT INTO `abc` VALUES ('39687042', '1', '1', '1', '1', '1', '1', 991.00, '中国农业银行', '1');
INSERT INTO `abc` VALUES ('62851907', '1', '1', '1', '', '1', '1', 1.00, '中国农业银行', '1');
INSERT INTO `abc` VALUES ('47381906', '1', '1', '1', '1', '1', '1', 1.00, '中国农业银行', '1');
INSERT INTO `abc` VALUES ('07154296', '2', '2', '2', '2', '2', '2', 2.00, '中国农业银行', '2');
INSERT INTO `abc` VALUES ('49851630', '5', '5', '5', '5', '5', '5', 5.00, '中国农业银行', '1');

-- ----------------------------
-- Table structure for iabc
-- ----------------------------
DROP TABLE IF EXISTS `iabc`;
CREATE TABLE `iabc`  (
  `code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '账号',
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `country` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '国家',
  `province` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '省份',
  `street` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '街道',
  `house` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '门牌号',
  `money` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '余额',
  `bank` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '开户行'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of iabc
-- ----------------------------
INSERT INTO `iabc` VALUES ('4894894', '李四', '456789', '印尼', '美国省', '幸福大道', 's002', '5000', NULL);
INSERT INTO `iabc` VALUES ('ab067f21', '1', '1', '1', '1', '1', '1', '0', NULL);
INSERT INTO `iabc` VALUES ('1c2711cb', '1', '1', '1', '1', '1', '1', '0', NULL);
INSERT INTO `iabc` VALUES ('907b33a9', '1', '1', '1', '1', '1', '1', '0', NULL);
INSERT INTO `iabc` VALUES ('s', 's', 's', 's', 's', 's', 's', 's', NULL);
INSERT INTO `iabc` VALUES ('1', '1', '1', '1', '1', '1', '1', '31', NULL);
INSERT INTO `iabc` VALUES ('56713516', '5', '555', '5555', '555', '55', '55', '55', NULL);
INSERT INTO `iabc` VALUES ('10747243', '1', 'z', 'z', 'zz', 'z', 'z', 'z', NULL);
INSERT INTO `iabc` VALUES ('01277563', '1', '1', '1', '1', '1', '1', '1', NULL);
INSERT INTO `iabc` VALUES ('50455411', '1', '1', '1', '1', '1', '1', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('77405116', '5', '6', '6', '6', '6', '6', '6', '中国工商银行');
INSERT INTO `iabc` VALUES ('75451760', '5', '6', '3', '3', '3', '3', '3', '中国工商银行');
INSERT INTO `iabc` VALUES ('56316616', '89', '99', '99', '99', '6999', '9999', '99999', '中国工商银行');
INSERT INTO `iabc` VALUES ('42544011', '5', '12', '12', '12', '12', '12', '12', '中国工商银行');
INSERT INTO `iabc` VALUES ('34141716', '11', '1', '1', '1', '1', '1', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('47236270', '1', '1', '1', '1', '1', '1', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('76025204', '1', '1', '1', '1', '11', '1', '289', '中国工商银行');
INSERT INTO `iabc` VALUES ('44542425', '132', '1', '1', '1', '1', '1', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('36301057', '1', '', '0', '0', '', '', '', '中国工商银行');
INSERT INTO `iabc` VALUES ('71762515', '0', '', '', '', '', '', '', '中国工商银行');
INSERT INTO `iabc` VALUES ('73247155', '1', '1', '1', '1', '1', '1', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('31716040', '1', '1', '2', '23', '5', '8', '1', '中国工商银行');
INSERT INTO `iabc` VALUES ('08159674', '1', '1', '1', '1', '1', '1', '90', '中国工商银行');
INSERT INTO `iabc` VALUES ('31206948', '1', '1', '1', '1', '1', '1', '111', '中国工商银行');

SET FOREIGN_KEY_CHECKS = 1;
