<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('ourdata2.db');
      }
   }
   $db = new MyDB();
   $trapdata =<<<EOF
      CREATE TABLE IF NOT EXISTS finalproject(IPADDRESS VARCHAR NOT NULL,VLAN VARCHAR NOT NULL,ntime INT NOT NULL,PORT INT,MACS VARCHAR);
EOF;
$result = $db->exec($trapdata);
   if(!$result){
       $db->lastErrorMsg();
   }
$manager =<<<EOF
      CREATE TABLE IF NOT EXISTS manager(ip VARCHAR NOT NULL,port INT NOT NULL,community STRING NOT NULL,version VARCHAR NOT NULL,firstprob VARCHAR NULL,lastprob VARCHAR NULL);
EOF;
$result = $db->exec($manager);
   if(!$result){
       $db->lastErrorMsg();
   }
   ?>
