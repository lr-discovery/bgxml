#!/bin/bash
echo 'Bg test script'
echo '--------------'
echo
echo 'Service wsdl saved to TestOutputWsdl.xml'
curl http://localhost:5000/soap/bgservice/reflection?wsdl > TestOutputWsdl.xml
echo
echo
echo 'Inputed good xml'
cat BgTest.xml
echo
echo 'Returned xml saved to TestOutputGood.xml'
curl --data @BgTest.xml http://localhost:5000/soap/bgservice/reflection > TestOutputGood.xml
echo
echo
echo 'Inputed bad xml'
cat BgBad.xml
echo
echo
echo 'Returned xml saved to TestOutputBad.xml'
curl --data @BgBad.xml http://localhost:5000/soap/bgservice/reflection > TestOutputBad.xml
exit
