---
layout: page
title: " デベロッパーズガイド"
---
<!-- Title: シリアライザ名とROS/ROS2メッセージ型 -->
#contents

ROS,ROS2通信機能を使用する場合、以下のROS/ROS2メッセージ型に対応のシリアライザをOpenRTM-aistは備えています。以下のメッセージ型以外が必要な場合は、そのメッセージ型に変換するシリアライザを独自に実装してください。

<table class="table-alt">
  <tr>
    <th>シリアライザ名</th>
    <th>RTMデータ型</th>
    <th>ROS,ROS2メッセージ型</th>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32,<br> ros2:std_msgs/Float32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Float32</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float64,<br> ros2:std_msgs/Float64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Float64</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int8,<br> ros2:std_msgs/Int8</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Int8</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int16,<br> ros2:std_msgs/Int16</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/Int16</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int32,<br> ros2:std_msgs/Int32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt8</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int64,<br> ros2:std_msgs/Int64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt16</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt32,<br> ros2:std_msgs/UInt32</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt32</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt64,<br> ros2:std_msgs/UInt64</td>
    <td>TimedState,TimedShort,<br> TimedLong,TimedUShort,<br> TimedULong,TimedFloat,<br> TimedDouble</td>
    <td>std_msgs/UInt64</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32MultiArray,<br> ros2:std_msgs/Float32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float32MultiArray,<br> ros2:std_msgs/Float32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Float64MultiArray,<br> ros2:std_msgs/Float64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq, TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Float64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int8MultiArray,<br> ros2:std_msgs/Int8MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int8MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int16MultiArray,<br> ros2:std_msgs/nt16MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int16MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int32MultiArray,<br> ros2:std_msgs/Int32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/Int64MultiArray,<br> ros2:std_msgs/Int64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/Int64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt8MultiArray,<br> ros2:std_msgs/UInt8MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt8MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt16MultiArray,<br> ros2:std_msgs/UInt16MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt16MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt32MultiArray,<br> ros2:std_msgs/UInt32MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt32MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/UInt64MultiArray,<br> ros2:std_msgs/UInt64MultiArray</td>
    <td>TimedShortSeq,TimedLongSeq,<br> TimedUShortSeq,TimedULongSeq,<br> TimedFloatSeq,TimedDoubleSeq</td>
    <td>std_msgs/UInt64MultiArray</td>
  </tr>
  <tr>
    <td>ros:std_msgs/String,<br> ros2:std_msgs/String</td>
    <td>TimedString</td>
    <td>std_msgs/String</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/PointStamped,<br> ros2:geometry_msgs/PointStamped</td>
    <td>TimedPoint3D</td>
    <td>geometry_msgs/PointStamped</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/QuaternionStamped,<br> ros2:geometry_msgs/QuaternionStamped</td>
    <td>TimedQuaternion</td>
    <td>geometry_msgs/QuaternionStamped</td>
  </tr>
  <tr>
    <td>ros:geometry_msgs/Vector3Stamped,<br> ros2:geometry_msgs/Vector3Stamped</td>
    <td>TimedVector3D</td>
    <td>geometry_msgs/Vector3Stamped</td>
  </tr>
  <tr>
    <td>ros:sensor_msgs/Image,<br> ros2:sensor_msgs/Image</td>
    <td>CameraImage</td>
    <td>sensor_msgs/Image</td>
  </tr>
</table>



