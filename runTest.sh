#!/bin/bash
echo 'Bg test script'
echo '--------------'
echo 'Inputed good xml'
cat BgTest.xml
echo 'Returned result'
curl --data @BgTest.xml http://localhost:5000/soap/bgservice/reflection
echo 'Inputed bad xml'
cat BgBad.xml
echo
echo 'Returned result'
curl --data @BgBad.xml http://localhost:5000/soap/bgservice/reflection
exit
