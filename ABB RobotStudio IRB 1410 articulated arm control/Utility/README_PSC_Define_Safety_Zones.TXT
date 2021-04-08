
	 The file PSC_Define_Safety_Zones.sys module makes it possible to configure/define Safety Zones 
     that can be imported into the Safemove configurator.
     
     The configuration is in three parts:
     1. additional supervision Toolpoints of the TCP
     2. Monitoring Tool Zone
     3. Safe Tool Zone
     
     The PSC_Define_Safety_Zones.sys module must be installed into the Robot System to be able
     to import it into the Safemove configurator.
     To install it you can use RobotStudio, the FlexPendant or editing the SYS.cfg file.
     After editing the controller must be restarted.
     The file PSC_Define_Safety_Zones.sys must first be downloaded to the controller.
     
	 ROBOTSTUDIO:
	 open the "Controller" settings via the Configuration Editor and edit 
	 the "Automatic loading of Modules(s).
	 
	 FLEXPENDANT: 
	 open the "Controller" settings via the Control Panel and the Configuration, edit
	 the "Automatic loading of Modules(s).
	 
	 EDITING SYS.cfg:
	 the below text can be added into the SYS.cfg file, the path
	 to the file can be change to your own choice.
     CAB_TASK_MODULES:
      -File "HOME:/PSC_Define_Safety_Zones.sys"\
      -ModName "PSC_Define_Safety_Zones" -Task "T_ROB1"
	 
 
	 EXAMPLE:
	  
        !**********************************************************
        !*  Pos definitions for addtional supervision of the TCP  *
        !**********************************************************
		TASK PERS pos posPSCTool0{8}:=[[-80,-850,0],[-1200,520,0],[740,1000,0],[1111,-333,0],[-800,-850,400],[-1111,590,400],[747,1032,400],[1111,-333,400]];

        !**********************************************************
        !*  Monitor Tool Zone definition						  *
        !**********************************************************
        TASK PERS robtarget pMTZ_Set_1_Pos_1:=[[100,-400,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pMTZ_Set_1_Pos_2:=[[750,-400,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pMTZ_Set_1_Pos_3:=[[750,-1200,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pMTZ_Set_1_Pos_4:=[[100,-1200,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];

        !**********************************************************
        !*  Safe Tool Zone definition						      *
        !**********************************************************
        TASK PERS robtarget pSTZ_Set_1_Pos_1:=[[100,-400,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pSTZ_Set_1_Pos_2:=[[750,-400,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pSTZ_Set_1_Pos_3:=[[750,-1200,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];
        TASK PERS robtarget pSTZ_Set_1_Pos_4:=[[100,-1200,0],[0,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]];

	 END EXAMPLE   




















