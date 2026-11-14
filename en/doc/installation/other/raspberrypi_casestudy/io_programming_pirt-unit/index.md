---
layout: page
title: io programming using pirt-unit
---

<!-- Title: PiRT-Unitを利用したIOプログラミング -->
#contents

This Book explains how to use Raspberry Pi together with PiRT-Unit from OpenRTM-aist.

## Using PiRT-Unit

PiRT-Unit is an IO expansion board for Raspberry Pi developed by AIST.
It is currently available from Win-Ei Electronics.

<!-- ウィン電子工業から購入することができます。 -->

- Win-Ei Electronics:  http://win-ei.com/
  - Raspberry Pi expansion board: http://cgi3.win-ei.com/wordpress/?page_id=135
    - Product name: Pi RT-Unit
    - Model number: RE-01
    - Price: \6,615 (tax included)

#clear
<div align="center"><a href="pirt-unit.png"><img src="pirt-unit.png" width="80%;"></a></div>
<div align="center"><strong>PiRT-Unit Overview</strong></div>

PiRT-Unit provides AD (4ch), DA (2ch), PWM (1ch), I2C (1ch), and RS232C/XBee (1ch).

<div align="center"><a href="pirt-unit_connectors.png"><img src="pirt-unit_connectors.png" width="80%;"></a></div>
<div align="center"><strong>PiRT-Unit Input/Output Connector Layout Diagram</strong></div>

### Features

- Analog input (10-bit ADC x 4ch) available
- Analog output (12-bit DAC x 2ch) available
- PWM x1ch: RC servo motor available
- I2C serial communication available
- RS232C Dsub connector available
- XBee connection connector available (selectable with the above RS232C)
- 5V DC input: Power can be supplied to Raspberry Pi
  - An inexpensive AC adapter available from Akizuki Denshi, etc. can be used


### Specifications

<table class="table-alt">
  <tr>
    <th colspan="2" style="text-align: center;">Raspberry Pi Expansion IO Board</th>
  </tr>
  <tr>
    <td>AD converter</td>
    <td>10bit, 4ch <br> Chip: ADC104S021 <br> Sampling 200kHz</td>
  </tr>
  <tr>
    <td>DA converter</td>
    <td>12bit, 2ch <br> Chip MCP4822</td>
  </tr>
  <tr>
    <td>PWM output</td>
    <td>1ch, for RC servo motor drive <br> Photocoupler isolation</td>
  </tr>
  <tr>
    <td>RS232C</td>
    <td>D-SUB 9pin connector <br> Switchable with XBee using a jumper</td>
  </tr>
  <tr>
    <td>XBee</td>
    <td>XBee connection connector <br> XBee: Zigbee module manufactured by Digi International <br> Switchable with XBee using a jumper</td>
  </tr>
  <tr>
    <td>Power input</td>
    <td>5V DC input <br> Power can be supplied to Raspberry Pi <br> Operates even when powered from Raspberry Pi</td>
  </tr>
</table>


<div align="center"><a href="pirtunit_blockdiagram.png"><img src="pirtunit_blockdiagram.png" width="100%;"></a></div>
<div align="center"><strong>PiRT-Unit Circuit Block Diagram</strong></div>

<hr>

- [System Settings for PiRT-Unit](./system_setting_pirt-unit)
- [IO Test](./io_test)
- [Creating a Ministick Component](./create_ministick_comp)
- [Using an XBee Module with PiRT-Unit](./xbee_use_pirt-unit)
- [Using an I2C Device with PiRT-Unit](./i2c_device_use_pirt-unit)

