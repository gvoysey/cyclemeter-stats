from peewee import *

database = SqliteDatabase('Meter.db', **{})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Abtest(BaseModel):
    groupid = IntegerField(db_column='groupID', null=True)
    testid = PrimaryKeyField(db_column='testID', null=True)

    class Meta:
        db_table = 'abTest'


class Activity(BaseModel):
    activitydone = BooleanField(db_column='activityDone', null=True)
    activityid = PrimaryKeyField(db_column='activityID', null=True)
    activitynameid = IntegerField(db_column='activityNameID', null=True)
    activitynamestr = TextField(db_column='activityNameStr', null=True)
    activitynotesid = IntegerField(db_column='activityNotesID', null=True)
    activitynotesstr = TextField(db_column='activityNotesStr', null=True)
    activitytypeid = IntegerField(db_column='activityTypeID', null=True)
    appoffline = IntegerField(db_column='appOffline', null=True)
    bikeid = IntegerField(db_column='bikeID', null=True)
    calendareventid = TextField(db_column='calendarEventID', null=True)
    cooldowntimescount = IntegerField(db_column='coolDownTimesCount', null=True)
    crankcadencemaxtarget = IntegerField(db_column='crankCadenceMaxTarget', null=True)
    crankcadencemintarget = IntegerField(db_column='crankCadenceMinTarget', null=True)
    cycleoffroad = BooleanField(db_column='cycleOffRoad', null=True)
    dampenfastest = BooleanField(db_column='dampenFastest', null=True)
    dashboard = BlobField(null=True)
    distancemeasure = IntegerField(db_column='distanceMeasure', null=True)
    filterlocations = BooleanField(db_column='filterLocations', null=True)
    heartratemaxtarget = IntegerField(db_column='heartRateMaxTarget', null=True)
    heartratemintarget = IntegerField(db_column='heartRateMinTarget', null=True)
    insummaries = BooleanField(db_column='inSummaries', null=True)
    pacemaxtarget = DoubleField(db_column='paceMaxTarget', null=True)  # DOUBLE
    pacemintarget = UnknownField(db_column='paceMinTarget', null=True)  # DOUBLE
    powermaxtarget = IntegerField(db_column='powerMaxTarget', null=True)
    powermintarget = IntegerField(db_column='powerMinTarget', null=True)
    runcellbotleftstatsitemid = IntegerField(db_column='runCellBotLeftStatsItemID', null=True)
    runcelltopleftstatsitemid = IntegerField(db_column='runCellTopLeftStatsItemID', null=True)
    runcellweather = BooleanField(db_column='runCellWeather', null=True)
    selected = BooleanField(null=True)
    shoesid = IntegerField(db_column='shoesID', null=True)
    showprogresspage = BooleanField(db_column='showProgressPage', null=True)
    speedbased = BooleanField(db_column='speedBased', null=True)
    speedmaxtarget = UnknownField(db_column='speedMaxTarget', null=True)  # DOUBLE
    speedmintarget = UnknownField(db_column='speedMinTarget', null=True)  # DOUBLE
    splitdistanceintervalid = IntegerField(db_column='splitDistanceIntervalID', null=True)
    stopatend = BooleanField(db_column='stopAtEnd', null=True)
    stopdetection = IntegerField(db_column='stopDetection', null=True)
    stridecadencemaxtarget = UnknownField(db_column='strideCadenceMaxTarget', null=True)  # DOUBLE
    stridecadencemintarget = UnknownField(db_column='strideCadenceMinTarget', null=True)  # DOUBLE
    stridelength = UnknownField(db_column='strideLength', null=True)  # DOUBLE
    stridemeasure = IntegerField(db_column='strideMeasure', null=True)
    summaryactivityid = IntegerField(db_column='summaryActivityID', null=True)
    summarydashboard = BlobField(db_column='summaryDashboard', null=True)
    useindoors = IntegerField(db_column='useIndoors', null=True)
    usestepdistance = IntegerField(db_column='useStepDistance', null=True)
    usesteps = IntegerField(db_column='useSteps', null=True)
    usedasplanactivity = BooleanField(db_column='usedAsPlanActivity', null=True)
    warmuptimescount = IntegerField(db_column='warmUpTimesCount', null=True)
    workouttimescount = IntegerField(db_column='workoutTimesCount', null=True)

    class Meta:
        db_table = 'activity'


class Activityinterval(BaseModel):
    activityid = IntegerField(db_column='activityID', null=True)
    crankcadencemaxtarget = IntegerField(db_column='crankCadenceMaxTarget', null=True)
    crankcadencemintarget = IntegerField(db_column='crankCadenceMinTarget', null=True)
    heartratemaxtarget = IntegerField(db_column='heartRateMaxTarget', null=True)
    heartratemintarget = IntegerField(db_column='heartRateMinTarget', null=True)
    intervalgroupid = IntegerField(db_column='intervalGroupID', null=True)
    intervalindex = IntegerField(db_column='intervalIndex', null=True)
    intervalnameid = IntegerField(db_column='intervalNameID', null=True)
    intervalnamestr = TextField(db_column='intervalNameStr', null=True)
    intervaltypeid = IntegerField(db_column='intervalTypeID', null=True)
    latitude = UnknownField(null=True)  # DOUBLE
    length = UnknownField(null=True)  # DOUBLE
    lengthmeasure = IntegerField(db_column='lengthMeasure', null=True)
    longitude = UnknownField(null=True)  # DOUBLE
    pacemaxtarget = UnknownField(db_column='paceMaxTarget', null=True)  # DOUBLE
    pacemintarget = UnknownField(db_column='paceMinTarget', null=True)  # DOUBLE
    powermaxtarget = IntegerField(db_column='powerMaxTarget', null=True)
    powermintarget = IntegerField(db_column='powerMinTarget', null=True)
    runtime = UnknownField(db_column='runTime', null=True)  # DOUBLE
    speedmaxtarget = UnknownField(db_column='speedMaxTarget', null=True)  # DOUBLE
    speedmintarget = UnknownField(db_column='speedMinTarget', null=True)  # DOUBLE
    stridecadencemaxtarget = UnknownField(db_column='strideCadenceMaxTarget', null=True)  # DOUBLE
    stridecadencemintarget = UnknownField(db_column='strideCadenceMinTarget', null=True)  # DOUBLE

    class Meta:
        db_table = 'activityInterval'
        primary_key = CompositeKey('activityid', 'intervalgroupid', 'intervalindex')


class Activitytype(BaseModel):
    activitytypeid = PrimaryKeyField(db_column='activityTypeID', null=True)
    assignbike = BooleanField(db_column='assignBike', null=True)
    assignshoes = BooleanField(db_column='assignShoes', null=True)
    longratetimethreshold = UnknownField(db_column='longRateTimeThreshold', null=True)  # DOUBLE
    maxabdistance = UnknownField(db_column='maxABDistance', null=True)  # DOUBLE
    maxspeed = UnknownField(db_column='maxSpeed', null=True)  # DOUBLE
    modified = BooleanField(null=True)
    motionthreshold = UnknownField(db_column='motionThreshold', null=True)  # DOUBLE
    oldratedistancethreshold = UnknownField(db_column='oldRateDistanceThreshold', null=True)  # DOUBLE
    oldratetimethreshold = UnknownField(db_column='oldRateTimeThreshold', null=True)  # DOUBLE
    ratedistancethreshold = UnknownField(db_column='rateDistanceThreshold', null=True)  # DOUBLE
    ratetimethreshold = UnknownField(db_column='rateTimeThreshold', null=True)  # DOUBLE
    stoppeddistancethreshold = UnknownField(db_column='stoppedDistanceThreshold', null=True)  # DOUBLE
    stoppedtimethreshold = UnknownField(db_column='stoppedTimeThreshold', null=True)  # DOUBLE

    class Meta:
        db_table = 'activityType'


class Activityzone(BaseModel):
    zoneindex = IntegerField(db_column='zoneIndex', null=True)
    zoneminvalue = UnknownField(db_column='zoneMinValue', null=True)  # DOUBLE
    zonenameid = IntegerField(db_column='zoneNameID', null=True)
    zonenamestr = TextField(db_column='zoneNameStr', null=True)
    zonesetid = IntegerField(db_column='zoneSetID', null=True)

    class Meta:
        db_table = 'activityZone'
        primary_key = CompositeKey('zoneindex', 'zonesetid')


class Activityzoneset(BaseModel):
    automatic = BooleanField(null=True)
    selected = BooleanField(null=True)
    zonemaxvalue = UnknownField(db_column='zoneMaxValue', null=True)  # DOUBLE
    zonesetid = PrimaryKeyField(db_column='zoneSetID', null=True)
    zonesetnameid = IntegerField(db_column='zoneSetNameID', null=True)
    zonesetnamestr = TextField(db_column='zoneSetNameStr', null=True)
    zonesettypeid = IntegerField(db_column='zoneSetTypeID', null=True)

    class Meta:
        db_table = 'activityZoneSet'


class Altitude(BaseModel):
    altitude = UnknownField(null=True)  # DOUBLE
    climbspeed = UnknownField(db_column='climbSpeed', null=True)  # DOUBLE
    distancedelta = UnknownField(db_column='distanceDelta', null=True)  # DOUBLE
    longaltitude = UnknownField(db_column='longAltitude', null=True)  # DOUBLE
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'altitude'
        primary_key = CompositeKey('runid', 'sequenceid')


class Announcements(BaseModel):
    announcementsenabled = BooleanField(db_column='announcementsEnabled', null=True)
    audioducking = BooleanField(db_column='audioDucking', null=True)
    awakenbluetoothaudio = IntegerField(db_column='awakenBluetoothAudio', null=True)
    begininterval = BooleanField(db_column='beginInterval', null=True)
    beginintervalnumber = BooleanField(db_column='beginIntervalNumber', null=True)
    beginintervalrepetition = BooleanField(db_column='beginIntervalRepetition', null=True)
    beginsplit = BooleanField(db_column='beginSplit', null=True)
    distanceintervalid = IntegerField(db_column='distanceIntervalID', null=True)
    distanceitemlist = TextField(db_column='distanceItemList', null=True)
    endinterval = BooleanField(db_column='endInterval', null=True)
    endintervalitemlist = TextField(db_column='endIntervalItemList', null=True)
    endsplit = BooleanField(db_column='endSplit', null=True)
    endsplititemlist = TextField(db_column='endSplitItemList', null=True)
    fulldistance = BooleanField(db_column='fullDistance', null=True)
    halfdistance = BooleanField(db_column='halfDistance', null=True)
    interruptipod = BooleanField(db_column='interruptIPod', null=True)
    interruptipodui = BooleanField(db_column='interruptIPodUI', null=True)
    key = PrimaryKeyField(null=True)
    ondemand = IntegerField(db_column='onDemand', null=True)
    ondemanditemlist = TextField(db_column='onDemandItemList', null=True)
    onpassingevent = BooleanField(db_column='onPassingEvent', null=True)
    shorten = BooleanField(null=True)
    startstop = IntegerField(db_column='startStop', null=True)
    target = IntegerField(null=True)
    timeintervalid = IntegerField(db_column='timeIntervalID', null=True)
    timeitemlist = TextField(db_column='timeItemList', null=True)
    volume = UnknownField(null=True)  # DOUBLE

    class Meta:
        db_table = 'announcements'


class Backup(BaseModel):
    askinstalltime = UnknownField(db_column='askInstallTime', null=True)  # TIMESTAMP
    askedautosave = BooleanField(db_column='askedAutoSave', null=True)
    autosavefrequency = IntegerField(db_column='autoSaveFrequency', null=True)
    key = PrimaryKeyField(null=True)
    savetime = UnknownField(db_column='saveTime', null=True)  # TIMESTAMP
    usecellular = BooleanField(db_column='useCellular', null=True)

    class Meta:
        db_table = 'backup'


class Bike(BaseModel):
    bikeid = PrimaryKeyField(db_column='bikeID', null=True)
    date = UnknownField(null=True)  # TIMESTAMP
    initialdistance = UnknownField(db_column='initialDistance', null=True)  # DOUBLE
    name = TextField(null=True)
    wheelsize = UnknownField(db_column='wheelSize', null=True)  # DOUBLE
    wheelsizeshowcircumference = BooleanField(db_column='wheelSizeShowCircumference', null=True)
    wheelsizeunits = IntegerField(db_column='wheelSizeUnits', null=True)

    class Meta:
        db_table = 'bike'


class Bikespeedstopdetection(BaseModel):
    action = IntegerField(null=True)
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'bikeSpeedStopDetection'
        primary_key = CompositeKey('runid', 'sequenceid')


class Calendar(BaseModel):
    alldayenabled = BooleanField(db_column='allDayEnabled', null=True)
    availability = IntegerField(null=True)
    calendartitle = TextField(db_column='calendarTitle', null=True)
    calendartype = IntegerField(db_column='calendarType', null=True)
    firstweekday = IntegerField(db_column='firstWeekday', null=True)
    key = PrimaryKeyField(null=True)
    noteitems = TextField(db_column='noteItems', null=True)
    syncenabled = BooleanField(db_column='syncEnabled', null=True)
    titleitems = TextField(db_column='titleItems', null=True)

    class Meta:
        db_table = 'calendar'


class Competitor(BaseModel):
    competitorid = PrimaryKeyField(db_column='competitorID', null=True)
    competitoriconid = IntegerField(db_column='competitorIconID', null=True)
    initials = TextField(null=True)
    name = TextField(null=True)
    share = IntegerField(null=True)

    class Meta:
        db_table = 'competitor'


class Coordinate(BaseModel):
    distancedelta = UnknownField(db_column='distanceDelta', null=True)  # DOUBLE
    latitude = UnknownField(null=True)  # DOUBLE
    longspeed = UnknownField(db_column='longSpeed', null=True)  # DOUBLE
    longitude = UnknownField(null=True)  # DOUBLE
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    speed = UnknownField(null=True)  # DOUBLE
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'coordinate'
        primary_key = CompositeKey('runid', 'sequenceid')


class Dailymile(BaseModel):
    accesstoken = TextField(db_column='accessToken', null=True)
    announceallowme = BooleanField(db_column='announceAllowMe', null=True)
    dailymileannouncementstype = IntegerField(db_column='dailymileAnnouncementsType', null=True)
    dailymileenabled = BooleanField(db_column='dailymileEnabled', null=True)
    displayname = TextField(db_column='displayName', null=True)
    key = PrimaryKeyField(null=True)
    promptondone = BooleanField(db_column='promptOnDone', null=True)
    sendatdistanceinterval = IntegerField(db_column='sendAtDistanceInterval', null=True)
    sendatdistanceintervalmessageitems = TextField(db_column='sendAtDistanceIntervalMessageItems', null=True)
    sendatdistanceintervaltitleitems = TextField(db_column='sendAtDistanceIntervalTitleItems', null=True)
    sendattimeinterval = IntegerField(db_column='sendAtTimeInterval', null=True)
    sendattimeintervalmessageitems = TextField(db_column='sendAtTimeIntervalMessageItems', null=True)
    sendattimeintervaltitleitems = TextField(db_column='sendAtTimeIntervalTitleItems', null=True)
    sendendinterval = BooleanField(db_column='sendEndInterval', null=True)
    sendendintervalmessageitems = TextField(db_column='sendEndIntervalMessageItems', null=True)
    sendendintervaltitleitems = TextField(db_column='sendEndIntervalTitleItems', null=True)
    sendendsplit = BooleanField(db_column='sendEndSplit', null=True)
    sendendsplitmessageitems = TextField(db_column='sendEndSplitMessageItems', null=True)
    sendendsplittitleitems = TextField(db_column='sendEndSplitTitleItems', null=True)
    sendoncontinue = BooleanField(db_column='sendOnContinue', null=True)
    sendoncontinuemessageitems = TextField(db_column='sendOnContinueMessageItems', null=True)
    sendoncontinuetitleitems = TextField(db_column='sendOnContinueTitleItems', null=True)
    sendondone = BooleanField(db_column='sendOnDone', null=True)
    sendondonemessageitems = TextField(db_column='sendOnDoneMessageItems', null=True)
    sendondonetitleitems = TextField(db_column='sendOnDoneTitleItems', null=True)
    sendonstart = BooleanField(db_column='sendOnStart', null=True)
    sendonstartmessageitems = TextField(db_column='sendOnStartMessageItems', null=True)
    sendonstarttitleitems = TextField(db_column='sendOnStartTitleItems', null=True)
    sendonstop = BooleanField(db_column='sendOnStop', null=True)
    sendonstopmessageitems = TextField(db_column='sendOnStopMessageItems', null=True)
    sendonstoptitleitems = TextField(db_column='sendOnStopTitleItems', null=True)
    sharemap = BooleanField(db_column='shareMap', null=True)
    userwhitelist = TextField(db_column='userWhiteList', null=True)
    username = TextField(null=True)

    class Meta:
        db_table = 'dailymile'


class Dashboard(BaseModel):
    dashboard = BlobField(null=True)
    dashboardid = PrimaryKeyField(db_column='dashboardID', null=True)

    class Meta:
        db_table = 'dashboard'


class Emailupdates(BaseModel):
    emailupdatesenabled = BooleanField(db_column='emailUpdatesEnabled', null=True)
    fromnoreply = BooleanField(db_column='fromNoReply', null=True)
    key = PrimaryKeyField(null=True)
    promptondone = BooleanField(db_column='promptOnDone', null=True)
    sendatdistanceinterval = IntegerField(db_column='sendAtDistanceInterval', null=True)
    sendatdistanceintervalitems = TextField(db_column='sendAtDistanceIntervalItems', null=True)
    sendattimeinterval = IntegerField(db_column='sendAtTimeInterval', null=True)
    sendattimeintervalitems = TextField(db_column='sendAtTimeIntervalItems', null=True)
    sendendinterval = BooleanField(db_column='sendEndInterval', null=True)
    sendendintervalitems = TextField(db_column='sendEndIntervalItems', null=True)
    sendendsplit = BooleanField(db_column='sendEndSplit', null=True)
    sendendsplititems = TextField(db_column='sendEndSplitItems', null=True)
    sendoncontinue = BooleanField(db_column='sendOnContinue', null=True)
    sendoncontinueitems = TextField(db_column='sendOnContinueItems', null=True)
    sendondone = BooleanField(db_column='sendOnDone', null=True)
    sendondoneitems = TextField(db_column='sendOnDoneItems', null=True)
    sendonstart = BooleanField(db_column='sendOnStart', null=True)
    sendonstartitems = TextField(db_column='sendOnStartItems', null=True)
    sendonstop = BooleanField(db_column='sendOnStop', null=True)
    sendonstopitems = TextField(db_column='sendOnStopItems', null=True)
    tolist = TextField(db_column='toList', null=True)

    class Meta:
        db_table = 'emailUpdates'


class Emailupdatesmailbox(BaseModel):
    message = TextField(null=True)
    messageid = PrimaryKeyField(db_column='messageID', null=True)
    subject = TextField(null=True)
    timestamp = UnknownField(null=True)  # TIMESTAMP
    tolist = TextField(db_column='toList', null=True)

    class Meta:
        db_table = 'emailUpdatesMailbox'


class Facebook(BaseModel):
    accesstoken = TextField(db_column='accessToken', null=True)
    announceallowme = BooleanField(db_column='announceAllowMe', null=True)
    expirationinterval = UnknownField(db_column='expirationInterval', null=True)  # DOUBLE
    facebookannouncementstype = IntegerField(db_column='facebookAnnouncementsType', null=True)
    facebookenabled = BooleanField(db_column='facebookEnabled', null=True)
    key = PrimaryKeyField(null=True)
    postatdistance = BooleanField(db_column='postAtDistance', null=True)
    postatdistanceinterval = IntegerField(db_column='postAtDistanceInterval', null=True)
    postatdistanceintervaldescriptionitems = TextField(db_column='postAtDistanceIntervalDescriptionItems', null=True)
    postatdistanceintervaltitleitems = TextField(db_column='postAtDistanceIntervalTitleItems', null=True)
    postattime = BooleanField(db_column='postAtTime', null=True)
    postattimeinterval = IntegerField(db_column='postAtTimeInterval', null=True)
    postattimeintervaldescriptionitems = TextField(db_column='postAtTimeIntervalDescriptionItems', null=True)
    postattimeintervaltitleitems = TextField(db_column='postAtTimeIntervalTitleItems', null=True)
    postendinterval = BooleanField(db_column='postEndInterval', null=True)
    postendintervaldescriptionitems = TextField(db_column='postEndIntervalDescriptionItems', null=True)
    postendintervaltitleitems = TextField(db_column='postEndIntervalTitleItems', null=True)
    postendsplit = BooleanField(db_column='postEndSplit', null=True)
    postendsplitdescriptionitems = TextField(db_column='postEndSplitDescriptionItems', null=True)
    postendsplittitleitems = TextField(db_column='postEndSplitTitleItems', null=True)
    postoncontinue = BooleanField(db_column='postOnContinue', null=True)
    postoncontinuedescriptionitems = TextField(db_column='postOnContinueDescriptionItems', null=True)
    postoncontinuetitleitems = TextField(db_column='postOnContinueTitleItems', null=True)
    postondone = BooleanField(db_column='postOnDone', null=True)
    postondonedescriptionitems = TextField(db_column='postOnDoneDescriptionItems', null=True)
    postondonetitleitems = TextField(db_column='postOnDoneTitleItems', null=True)
    postonstart = BooleanField(db_column='postOnStart', null=True)
    postonstartdescriptionitems = TextField(db_column='postOnStartDescriptionItems', null=True)
    postonstarttitleitems = TextField(db_column='postOnStartTitleItems', null=True)
    postonstop = BooleanField(db_column='postOnStop', null=True)
    postonstopdescriptionitems = TextField(db_column='postOnStopDescriptionItems', null=True)
    postonstoptitleitems = TextField(db_column='postOnStopTitleItems', null=True)
    promptondone = BooleanField(db_column='promptOnDone', null=True)
    uid = TextField(null=True)
    username = TextField(db_column='userName', null=True)
    userwhitelist = TextField(db_column='userWhiteList', null=True)

    class Meta:
        db_table = 'facebook'


class Locationblob(BaseModel):
    blob = BlobField(null=True)
    blobid = IntegerField(db_column='blobID', null=True)
    runid = IntegerField(db_column='runID', null=True)

    class Meta:
        db_table = 'locationBlob'
        primary_key = CompositeKey('blobid', 'runid')


class Meter(BaseModel):
    appbuildnumber = TextField(db_column='appBuildNumber', null=True)
    appinstanceid = TextField(db_column='appInstanceID', null=True)
    applaunchcount = IntegerField(db_column='appLaunchCount', null=True)
    appversion = TextField(db_column='appVersion', null=True)
    asidentifier = TextField(db_column='asIdentifier', null=True)
    astrackingenabled = BooleanField(db_column='asTrackingEnabled', null=True)
    asktogetvoicetime = TextField(db_column='askToGetVoiceTime', null=True)
    askedsummarizedactivities = BooleanField(db_column='askedSummarizedActivities', null=True)
    askedtofollow = BooleanField(db_column='askedToFollow', null=True)
    bikespeedstoppedthreshold = UnknownField(db_column='bikeSpeedStoppedThreshold', null=True)  # DOUBLE
    cintervalgroupid = IntegerField(db_column='cIntervalGroupID', null=True)
    cintervalgrouptimesrun = IntegerField(db_column='cIntervalGroupTimesRun', null=True)
    cintervalindex = IntegerField(db_column='cIntervalIndex', null=True)
    capabilities = BlobField(null=True)
    coordmaxbtoacdistance = UnknownField(db_column='coordMaxBToACDistance', null=True)  # DOUBLE
    currentrunid = IntegerField(db_column='currentRunID', null=True)
    dbversion = IntegerField(db_column='dbVersion', null=True)
    didsetupelite = BooleanField(db_column='didSetupElite', null=True)
    elitepurchasetime = UnknownField(db_column='elitePurchaseTime', null=True)  # TIMESTAMP
    eliteupgradetime = UnknownField(db_column='eliteUpgradeTime', null=True)  # TIMESTAMP
    firstusetime = UnknownField(db_column='firstUseTime', null=True)  # TIMESTAMP
    firstuseversion = TextField(db_column='firstUseVersion', null=True)
    flashnewschecktime = UnknownField(db_column='flashNewsCheckTime', null=True)  # TIMESTAMP
    generaldict = TextField(db_column='generalDict', null=True)
    historysavedactivities = TextField(db_column='historySavedActivities', null=True)
    historysavedactivity = IntegerField(db_column='historySavedActivity', null=True)
    historysavedgroup = IntegerField(db_column='historySavedGroup', null=True)
    historysavedsummary = IntegerField(db_column='historySavedSummary', null=True)
    ipadapplaunchcount = IntegerField(db_column='iPadAppLaunchCount', null=True)
    ipadfirstuse = BooleanField(db_column='iPadFirstUse', null=True)
    iphoneapplaunchcount = IntegerField(db_column='iPhoneAppLaunchCount', null=True)
    key = PrimaryKeyField(null=True)
    lastimportcompetitorid = IntegerField(db_column='lastImportCompetitorID', null=True)
    lastphonedisplayheight = IntegerField(db_column='lastPhoneDisplayHeight', null=True)
    lastphonesizeretina4 = BooleanField(db_column='lastPhoneSizeRetina4', null=True)
    maxsensorage = UnknownField(db_column='maxSensorAge', null=True)  # DOUBLE
    minaltitudemove = UnknownField(db_column='minAltitudeMove', null=True)  # DOUBLE
    mincoordmove = UnknownField(db_column='minCoordMove', null=True)  # DOUBLE
    mingpsstatusforstart = UnknownField(db_column='minGPSStatusForStart', null=True)  # DOUBLE
    minhbarsforoutliers = UnknownField(db_column='minHBarsForOutliers', null=True)  # DOUBLE
    minoutlierdistance = UnknownField(db_column='minOutlierDistance', null=True)  # DOUBLE
    modtime = UnknownField(db_column='modTime', null=True)  # TIMESTAMP
    newsreadtime = UnknownField(db_column='newsReadTime', null=True)  # TIMESTAMP
    nonogpswarning = BooleanField(db_column='noNoGPSWarning', null=True)
    notes = TextField(null=True)
    onstartpostid = TextField(db_column='onStartPostID', null=True)
    pedometersavedspan = IntegerField(db_column='pedometerSavedSpan', null=True)
    planpaneviewindex = IntegerField(db_column='planPaneViewIndex', null=True)
    prolegacy = BooleanField(db_column='proLegacy', null=True)
    proupgradetime = UnknownField(db_column='proUpgradeTime', null=True)  # TIMESTAMP
    runsizvcdisplay = IntegerField(db_column='runSIZVCDisplay', null=True)
    runsizvczonesetid = IntegerField(db_column='runSIZVCZoneSetID', null=True)
    runstate = IntegerField(db_column='runState', null=True)
    selectedbikeid = IntegerField(db_column='selectedBikeID', null=True)
    selectedpathid = IntegerField(db_column='selectedPathID', null=True)
    selectedproductidsuffix = TextField(db_column='selectedProductIDSuffix', null=True)
    selectedrouteid = IntegerField(db_column='selectedRouteID', null=True)
    selectedshoesid = IntegerField(db_column='selectedShoesID', null=True)
    selectedtabnumber = IntegerField(db_column='selectedTabNumber', null=True)
    selectedvoiceid = TextField(db_column='selectedVoiceID', null=True)
    sensorsinterval = UnknownField(db_column='sensorsInterval', null=True)  # DOUBLE
    statsuploadtime = UnknownField(db_column='statsUploadTime', null=True)  # TIMESTAMP
    stopwatchpageindex = IntegerField(db_column='stopwatchPageIndex', null=True)
    taborder = TextField(db_column='tabOrder', null=True)
    targetlocationinnerdistance = UnknownField(db_column='targetLocationInnerDistance', null=True)  # DOUBLE
    targetlocationouterdistance = UnknownField(db_column='targetLocationOuterDistance', null=True)  # DOUBLE
    targetnagtime = UnknownField(db_column='targetNagTime', null=True)  # DOUBLE
    tickets = TextField(null=True)
    upgradevoicesinprogress = BooleanField(db_column='upgradeVoicesInProgress', null=True)
    userconsent = BooleanField(db_column='userConsent', null=True)
    watchkeepalivedayid = IntegerField(db_column='watchKeepAliveDayID', null=True)
    watchkeepalivetime = UnknownField(db_column='watchKeepAliveTime', null=True)  # DOUBLE

    class Meta:
        db_table = 'meter'


class Motionblob(BaseModel):
    blob = BlobField(null=True)
    blobid = IntegerField(db_column='blobID', null=True)
    runid = IntegerField(db_column='runID', null=True)

    class Meta:
        db_table = 'motionBlob'
        primary_key = CompositeKey('blobid', 'runid')


class Myfitnesspal(BaseModel):
    accesstoken = TextField(db_column='accessToken', null=True)
    doneitems = TextField(db_column='doneItems', null=True)
    donesend = IntegerField(db_column='doneSend', null=True)
    key = PrimaryKeyField(null=True)
    myfitnesspalenabled = BooleanField(db_column='myFitnessPalEnabled', null=True)
    refreshtoken = TextField(db_column='refreshToken', null=True)

    class Meta:
        db_table = 'myFitnessPal'


class Notify(BaseModel):
    key = PrimaryKeyField(null=True)
    notifyatdistanceinterval = IntegerField(db_column='notifyAtDistanceInterval', null=True)
    notifyatdistanceintervalitems = TextField(db_column='notifyAtDistanceIntervalItems', null=True)
    notifyattimeinterval = IntegerField(db_column='notifyAtTimeInterval', null=True)
    notifyattimeintervalitems = TextField(db_column='notifyAtTimeIntervalItems', null=True)
    notifybegininterval = BooleanField(db_column='notifyBeginInterval', null=True)
    notifybeginsplit = BooleanField(db_column='notifyBeginSplit', null=True)
    notifyenabled = BooleanField(db_column='notifyEnabled', null=True)
    notifyendinterval = BooleanField(db_column='notifyEndInterval', null=True)
    notifyendintervalitems = TextField(db_column='notifyEndIntervalItems', null=True)
    notifyendintervalkind = IntegerField(db_column='notifyEndIntervalKind', null=True)
    notifyendsplit = BooleanField(db_column='notifyEndSplit', null=True)
    notifyendsplititems = TextField(db_column='notifyEndSplitItems', null=True)
    notifygrandfather = BooleanField(db_column='notifyGrandfather', null=True)
    notifytarget = BooleanField(db_column='notifyTarget', null=True)

    class Meta:
        db_table = 'notify'


class Pedometerdata(BaseModel):
    dayid = PrimaryKeyField(db_column='dayID', null=True)
    done = BooleanField(null=True)
    steps = IntegerField(null=True)

    class Meta:
        db_table = 'pedometerData'


class Plan(BaseModel):
    calendarsync = BooleanField(db_column='calendarSync', null=True)
    currentactivityindex = IntegerField(db_column='currentActivityIndex', null=True)
    date = UnknownField(null=True)  # TIMESTAMP
    datetype = IntegerField(db_column='dateType', null=True)
    descid = IntegerField(db_column='descID', null=True)
    descstr = TextField(db_column='descStr', null=True)
    nameid = IntegerField(db_column='nameID', null=True)
    namestr = TextField(db_column='nameStr', null=True)
    planenabled = BooleanField(db_column='planEnabled', null=True)
    planid = PrimaryKeyField(db_column='planID', null=True)
    planindex = IntegerField(db_column='planIndex', null=True)
    plantypeid = IntegerField(db_column='planTypeID', null=True)
    weekday = IntegerField(null=True)

    class Meta:
        db_table = 'plan'


class Planactivity(BaseModel):
    activityid = IntegerField(db_column='activityID', null=True)
    activityindex = IntegerField(db_column='activityIndex', null=True)
    planid = IntegerField(db_column='planID', null=True)

    class Meta:
        db_table = 'planActivity'
        primary_key = CompositeKey('activityindex', 'planid')


class Purchase(BaseModel):
    originaltransactiondate = UnknownField(db_column='originalTransactionDate', null=True)  # TIMESTAMP
    originaltransactionidentifier = TextField(db_column='originalTransactionIdentifier', null=True)
    productidentifier = TextField(db_column='productIdentifier', null=True)
    transactiondate = UnknownField(db_column='transactionDate', null=True)  # TIMESTAMP
    transactionidentifier = TextField(db_column='transactionIdentifier', null=True)
    transactionreceipt = TextField(db_column='transactionReceipt', null=True)

    class Meta:
        db_table = 'purchase'


class Register(BaseModel):
    emailaddr = TextField(db_column='emailAddr', null=True)
    emaileveryrun = BooleanField(db_column='emailEveryRun', null=True)
    firstname = TextField(db_column='firstName', null=True)
    key = PrimaryKeyField(null=True)
    lastname = TextField(db_column='lastName', null=True)
    receivenews = BooleanField(db_column='receiveNews', null=True)
    regemailaddr = TextField(db_column='regEmailAddr', null=True)
    status = BooleanField(null=True)

    class Meta:
        db_table = 'register'


class Route(BaseModel):
    bmwenabled = BooleanField(db_column='bmwEnabled', null=True)
    competitorsenabled = BooleanField(db_column='competitorsEnabled', null=True)
    dashboard = BlobField(null=True)
    name = TextField(index=True, null=True)
    officialdistance = UnknownField(db_column='officialDistance', null=True)  # DOUBLE
    officialenabled = BooleanField(db_column='officialEnabled', null=True)
    officialrunid = IntegerField(db_column='officialRunID', null=True)
    officialtime = UnknownField(db_column='officialTime', null=True)  # DOUBLE
    routeid = PrimaryKeyField(db_column='routeID', null=True)
    showgraphsicons = BooleanField(db_column='showGraphsIcons', null=True)
    showmapicons = BooleanField(db_column='showMapIcons', null=True)
    useofficialdistance = BooleanField(db_column='useOfficialDistance', null=True)

    class Meta:
        db_table = 'route'


class Run(BaseModel):
    activityid = IntegerField(db_column='activityID', null=True)
    adjustedpower = IntegerField(db_column='adjustedPower', null=True)
    age = IntegerField(null=True)
    altitudefromaltimeter = BooleanField(db_column='altitudeFromAltimeter', null=True)
    altitudehasclimbspeed = BooleanField(db_column='altitudeHasClimbSpeed', null=True)
    altitudehasdistancedelta = BooleanField(db_column='altitudeHasDistanceDelta', null=True)
    altitudehaslongaltitude = BooleanField(db_column='altitudeHasLongAltitude', null=True)
    ascent = UnknownField(null=True)  # DOUBLE
    avgcrankrpm = IntegerField(db_column='avgCrankRPM', null=True)
    avgheartrate = IntegerField(db_column='avgHeartRate', null=True)
    avgpower = IntegerField(db_column='avgPower', null=True)
    avgstepspm = IntegerField(db_column='avgStepsPM', null=True)
    avgtemp = UnknownField(db_column='avgTemp', null=True)  # DOUBLE
    avgwheelrpm = IntegerField(db_column='avgWheelRPM', null=True)
    badgpstime = UnknownField(db_column='badGPSTime', null=True)  # DOUBLE
    batteryusage = UnknownField(db_column='batteryUsage', null=True)  # DOUBLE
    bikeid = IntegerField(db_column='bikeID', null=True)
    calendareventid = TextField(db_column='calendarEventID', null=True)
    calories = UnknownField(null=True)  # DOUBLE
    caloriesuseelevation = BooleanField(db_column='caloriesUseElevation', null=True)
    competitorid = IntegerField(db_column='competitorID', null=True)
    coordinatehasspeed = BooleanField(db_column='coordinateHasSpeed', null=True)
    dailymileentryid = TextField(db_column='dailymileEntryID', null=True)
    descent = UnknownField(null=True)  # DOUBLE
    distance = UnknownField(null=True)  # DOUBLE
    dontloadrundata = BooleanField(db_column='dontLoadRunData', null=True)
    facebookactionid = TextField(db_column='facebookActionID', null=True)
    facebookactiontype = TextField(db_column='facebookActionType', null=True)
    facebookobjectid = TextField(db_column='facebookObjectID', null=True)
    gendermale = BooleanField(db_column='genderMale', null=True)
    grosssteps = IntegerField(db_column='grossSteps', null=True)
    health = TextField(null=True)
    healthsaved = BooleanField(db_column='healthSaved', null=True)
    heartratefromhealth = BooleanField(db_column='heartRateFromHealth', null=True)
    import_ = BooleanField(db_column='import', null=True)
    importdict = TextField(db_column='importDict', null=True)
    locality = TextField(null=True)
    maxcrankrpm = IntegerField(db_column='maxCrankRPM', null=True)
    maxheartrate = IntegerField(db_column='maxHeartRate', null=True)
    maxpower = IntegerField(db_column='maxPower', null=True)
    maxspeed = UnknownField(db_column='maxSpeed', null=True)  # DOUBLE
    maxstepspm = IntegerField(db_column='maxStepsPM', null=True)
    maxtemp = UnknownField(db_column='maxTemp', null=True)  # DOUBLE
    maxwheelrpm = IntegerField(db_column='maxWheelRPM', null=True)
    minpace = UnknownField(db_column='minPace', null=True)  # DOUBLE
    mintemp = UnknownField(db_column='minTemp', null=True)  # DOUBLE
    notes = TextField(null=True)
    official = BooleanField(null=True)
    pathonly = BooleanField(db_column='pathOnly', null=True)
    pathname = TextField(null=True)
    peakpower10min = IntegerField(db_column='peakPower10Min', null=True)
    peakpower1hr = IntegerField(db_column='peakPower1Hr', null=True)
    peakpower1min = IntegerField(db_column='peakPower1Min', null=True)
    peakpower20min = IntegerField(db_column='peakPower20Min', null=True)
    peakpower20sec = IntegerField(db_column='peakPower20Sec', null=True)
    peakpower5min = IntegerField(db_column='peakPower5Min', null=True)
    powerintensity = UnknownField(db_column='powerIntensity', null=True)  # DOUBLE
    powerscore = IntegerField(db_column='powerScore', null=True)
    routeid = IntegerField(db_column='routeID', null=True)
    runeditflags = IntegerField(db_column='runEditFlags', null=True)
    runid = PrimaryKeyField(db_column='runID', null=True)
    runtime = UnknownField(db_column='runTime', index=True, null=True)  # DOUBLE
    shoesid = IntegerField(db_column='shoesID', null=True)
    starttime = UnknownField(db_column='startTime', index=True, null=True)  # TIMESTAMP
    starttimezone = TextField(db_column='startTimeZone', null=True)
    steps = IntegerField(null=True)
    stopdetection = BooleanField(db_column='stopDetection', null=True)
    stoppedtime = UnknownField(db_column='stoppedTime', null=True)  # DOUBLE
    stridelength = UnknownField(db_column='strideLength', null=True)  # DOUBLE
    thresholdpower = IntegerField(db_column='thresholdPower', null=True)
    useindoors = BooleanField(db_column='useIndoors', null=True)
    usestepdistance = BooleanField(db_column='useStepDistance', null=True)
    usesteps = BooleanField(db_column='useSteps', null=True)
    userhash = TextField(db_column='userHash', null=True)
    vo2max = UnknownField(db_column='vo2Max', null=True)  # DOUBLE
    weather = BlobField(null=True)
    weight = UnknownField(null=True)  # DOUBLE
    wheelsize = UnknownField(db_column='wheelSize', null=True)  # DOUBLE

    class Meta:
        db_table = 'run'


class Runinterval(BaseModel):
    distancedelta = UnknownField(db_column='distanceDelta', null=True)  # DOUBLE
    importascent = UnknownField(db_column='importAscent', null=True)  # DOUBLE
    importavgcyclecadence = IntegerField(db_column='importAvgCycleCadence', null=True)
    importavgheartrate = IntegerField(db_column='importAvgHeartRate', null=True)
    importavgpower = IntegerField(db_column='importAvgPower', null=True)
    importavgspeed = UnknownField(db_column='importAvgSpeed', null=True)  # DOUBLE
    importavgstepcadence = IntegerField(db_column='importAvgStepCadence', null=True)
    importcalories = UnknownField(db_column='importCalories', null=True)  # DOUBLE
    importdescent = UnknownField(db_column='importDescent', null=True)  # DOUBLE
    importdistance = UnknownField(db_column='importDistance', null=True)  # DOUBLE
    importmaxcyclecadence = IntegerField(db_column='importMaxCycleCadence', null=True)
    importmaxheartrate = IntegerField(db_column='importMaxHeartRate', null=True)
    importmaxpower = IntegerField(db_column='importMaxPower', null=True)
    importmaxspeed = UnknownField(db_column='importMaxSpeed', null=True)  # DOUBLE
    importmaxstepcadence = IntegerField(db_column='importMaxStepCadence', null=True)
    importruntime = UnknownField(db_column='importRunTime', null=True)  # DOUBLE
    importsteps = IntegerField(db_column='importSteps', null=True)
    importstoppedtime = UnknownField(db_column='importStoppedTime', null=True)  # DOUBLE
    intervalnameid = IntegerField(db_column='intervalNameID', null=True)
    intervalnamestr = TextField(db_column='intervalNameStr', null=True)
    intervaltypeid = IntegerField(db_column='intervalTypeID', null=True)
    origintervaltypeid = IntegerField(db_column='origIntervalTypeID', null=True)
    runid = IntegerField(db_column='runID', null=True)
    runtimedelta = UnknownField(db_column='runTimeDelta', null=True)  # DOUBLE
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'runInterval'
        primary_key = CompositeKey('runid', 'sequenceid')


class Runstate(BaseModel):
    runid = IntegerField(db_column='runID', null=True)
    runstate = IntegerField(db_column='runState', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    steps = IntegerField(null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'runState'
        primary_key = CompositeKey('runid', 'sequenceid')


class Sensor(BaseModel):
    abnetworktypeid = IntegerField(db_column='abNetworkTypeID', null=True)
    absensorsubtypeid = IntegerField(db_column='abSensorSubtypeID', null=True)
    absensortypeid = IntegerField(db_column='abSensorTypeID', null=True)
    antbridgeenabled = IntegerField(db_column='antBridgeEnabled', null=True)
    antdeviceid = IntegerField(db_column='antDeviceID', null=True)
    anttransmissiontype = IntegerField(db_column='antTransmissionType', null=True)
    bikecadenceenabled = IntegerField(db_column='bikeCadenceEnabled', null=True)
    bikepowerenabled = IntegerField(db_column='bikePowerEnabled', null=True)
    bikespeedenabled = IntegerField(db_column='bikeSpeedEnabled', null=True)
    btledeviceuuid = TextField(db_column='btleDeviceUUID', null=True)
    displayenabled = IntegerField(db_column='displayEnabled', null=True)
    elevationenabled = IntegerField(db_column='elevationEnabled', null=True)
    heartrateenabled = IntegerField(db_column='heartRateEnabled', null=True)
    name = TextField(null=True)
    temperatureenabled = IntegerField(db_column='temperatureEnabled', null=True)

    class Meta:
        db_table = 'sensor'
        primary_key = CompositeKey('abnetworktypeid', 'absensortypeid', 'antdeviceid', 'anttransmissiontype',
                                   'btledeviceuuid')


class Sensordata(BaseModel):
    accumwheelrevs = IntegerField(db_column='accumWheelRevs', null=True)
    crankrpm = IntegerField(db_column='crankRPM', null=True)
    heartrate = IntegerField(db_column='heartRate', null=True)
    power = IntegerField(null=True)
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    stepcount = IntegerField(db_column='stepCount', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE
    wheelrpm = IntegerField(db_column='wheelRPM', null=True)

    class Meta:
        db_table = 'sensorData'
        primary_key = CompositeKey('runid', 'sequenceid')


class Settings(BaseModel):
    appdistancemeasure = IntegerField(db_column='appDistanceMeasure', null=True)
    appmaptype = IntegerField(db_column='appMapType', null=True)
    appoffline = BooleanField(db_column='appOffline', null=True)
    appusecalories = BooleanField(db_column='appUseCalories', null=True)
    appusecelsius = BooleanField(db_column='appUseCelsius', null=True)
    appweightmeasure = IntegerField(db_column='appWeightMeasure', null=True)
    autoconnectsensors = BooleanField(db_column='autoConnectSensors', null=True)
    autoselectlastactivity = BooleanField(db_column='autoSelectLastActivity', null=True)
    awakenbluetoothaudio = BooleanField(db_column='awakenBluetoothAudio', null=True)
    badgpstimeenabled = BooleanField(db_column='badGPSTimeEnabled', null=True)
    badgpstimepercenttime = IntegerField(db_column='badGPSTimePercentTime', null=True)
    badgpstimetimelimit = UnknownField(db_column='badGPSTimeTimeLimit', null=True)  # DOUBLE
    barometricaltimeter = BooleanField(db_column='barometricAltimeter', null=True)
    batterysavertime = UnknownField(db_column='batterySaverTime', null=True)  # DOUBLE
    bestrunhas = IntegerField(db_column='bestRunHas', null=True)
    birthday = UnknownField(null=True)  # TIMESTAMP
    bluetooth = BooleanField(null=True)
    botgraphviewdisplayid = IntegerField(db_column='botGraphViewDisplayID', null=True)
    caloriesuseelevation = BooleanField(db_column='caloriesUseElevation', null=True)
    casiobuttondict = BlobField(db_column='casioButtonDict', null=True)
    casiodisconnectondone = BooleanField(db_column='casioDisconnectOnDone', null=True)
    casiopagelist = BlobField(db_column='casioPageList', null=True)
    chinagpsoffset = BooleanField(db_column='chinaGPSOffset', null=True)
    compressuploads = BooleanField(db_column='compressUploads', null=True)
    dampenascentdescent = BooleanField(db_column='dampenAscentDescent', null=True)
    defaultpathid = IntegerField(db_column='defaultPathID', null=True)
    defaultrouteid = IntegerField(db_column='defaultRouteID', null=True)
    distancemarkersenabled = BooleanField(db_column='distanceMarkersEnabled', null=True)
    gendermale = BooleanField(db_column='genderMale', null=True)
    gpximportuselocaltimezone = BooleanField(db_column='gpxImportUseLocalTimeZone', null=True)
    graphviewdisplayid3 = IntegerField(db_column='graphViewDisplayID3', null=True)
    graphviewdisplayid4 = IntegerField(db_column='graphViewDisplayID4', null=True)
    graphviewdisplayids = TextField(db_column='graphViewDisplayIDs', null=True)
    graphslimitenabled = BooleanField(db_column='graphsLimitEnabled', null=True)
    health = TextField(null=True)
    historydashboard = BlobField(db_column='historyDashboard', null=True)
    importcompetitorme = BooleanField(db_column='importCompetitorMe', null=True)
    indoorswarningenabled = BooleanField(db_column='indoorsWarningEnabled', null=True)
    intervalmarkersenabled = BooleanField(db_column='intervalMarkersEnabled', null=True)
    key = PrimaryKeyField(null=True)
    landscapemodeenabled = BooleanField(db_column='landscapeModeEnabled', null=True)
    landscapemodeui = BooleanField(db_column='landscapeModeUI', null=True)
    latestfacebook = BooleanField(db_column='latestFacebook', null=True)
    lowmemorywarningenabled = BooleanField(db_column='lowMemoryWarningEnabled', null=True)
    mapmode = IntegerField(db_column='mapMode', null=True)
    maptrackheading = BooleanField(db_column='mapTrackHeading', null=True)
    maptrafficenabled = BooleanField(db_column='mapTrafficEnabled', null=True)
    mapvendor = IntegerField(db_column='mapVendor', null=True)
    maxcrankrpm = IntegerField(db_column='maxCrankRPM', null=True)
    maxlocationaccuracy = BooleanField(db_column='maxLocationAccuracy', null=True)
    maxwheelrpm = IntegerField(db_column='maxWheelRPM', null=True)
    newrouteofficialdistance = UnknownField(db_column='newRouteOfficialDistance', null=True)  # DOUBLE
    newrouteofficialtime = UnknownField(db_column='newRouteOfficialTime', null=True)  # DOUBLE
    newsenabled = BooleanField(db_column='newsEnabled', null=True)
    periodicmapupload = BooleanField(db_column='periodicMapUpload', null=True)
    proximitysensingenabled = BooleanField(db_column='proximitySensingEnabled', null=True)
    proximitysensingui = BooleanField(db_column='proximitySensingUI', null=True)
    ratings = BooleanField(null=True)
    remotecontrol = BooleanField(db_column='remoteControl', null=True)
    rflktbacklightpercent = IntegerField(db_column='rflktBacklightPercent', null=True)
    rflktbacklighttime = UnknownField(db_column='rflktBacklightTime', null=True)  # DOUBLE
    rflktbuttondict = BlobField(db_column='rflktButtonDict', null=True)
    rflktcalibrationelevation = UnknownField(db_column='rflktCalibrationElevation', null=True)  # DOUBLE
    rflktelevationcalibration = IntegerField(db_column='rflktElevationCalibration', null=True)
    rflktpagelimit = IntegerField(db_column='rflktPageLimit', null=True)
    rflktpagelist = BlobField(db_column='rflktPageList', null=True)
    runstridelength = UnknownField(db_column='runStrideLength', null=True)  # DOUBLE
    runstridemeasure = IntegerField(db_column='runStrideMeasure', null=True)
    screenon = IntegerField(db_column='screenOn', null=True)
    sharemap = BooleanField(db_column='shareMap', null=True)
    smoothelevationgraph = BooleanField(db_column='smoothElevationGraph', null=True)
    speakapplevoice = TextField(db_column='speakAppleVoice', null=True)
    speakkind = IntegerField(db_column='speakKind', null=True)
    stopdetection = BooleanField(db_column='stopDetection', null=True)
    stopdetectioninexports = BooleanField(db_column='stopDetectionInExports', null=True)
    stopdetectionusesduplicatelocations = BooleanField(db_column='stopDetectionUsesDuplicateLocations', null=True)
    stopwatchblack = BooleanField(db_column='stopwatchBlack', null=True)
    stopwatchpagelist = BlobField(db_column='stopwatchPageList', null=True)
    stopwatchstatstextstyle = IntegerField(db_column='stopwatchStatsTextStyle', null=True)
    tcxlaps = IntegerField(db_column='tcxLaps', null=True)
    thresholdpower = IntegerField(db_column='thresholdPower', null=True)
    todayenabled = BooleanField(db_column='todayEnabled', null=True)
    todayitems = TextField(db_column='todayItems', null=True)
    topgraphviewdisplayid = IntegerField(db_column='topGraphViewDisplayID', null=True)
    useindoors = BooleanField(db_column='useIndoors', null=True)
    uselocationservices = BooleanField(db_column='useLocationServices', null=True)
    usestepdistance = BooleanField(db_column='useStepDistance', null=True)
    usesteps = BooleanField(db_column='useSteps', null=True)
    vo2max = UnknownField(db_column='vo2Max', null=True)  # DOUBLE
    voicesettings = BooleanField(db_column='voiceSettings', null=True)
    walkstridelength = UnknownField(db_column='walkStrideLength', null=True)  # DOUBLE
    walkstridemeasure = IntegerField(db_column='walkStrideMeasure', null=True)
    watchpagelist = BlobField(db_column='watchPageList', null=True)
    weight = UnknownField(null=True)  # DOUBLE
    wheelsize = UnknownField(db_column='wheelSize', null=True)  # DOUBLE
    wheelsizeshowcircumference = BooleanField(db_column='wheelSizeShowCircumference', null=True)
    wheelsizeunits = IntegerField(db_column='wheelSizeUnits', null=True)

    class Meta:
        db_table = 'settings'


class Shoes(BaseModel):
    date = UnknownField(null=True)  # TIMESTAMP
    initialdistance = UnknownField(db_column='initialDistance', null=True)  # DOUBLE
    name = TextField(null=True)
    retired = BooleanField(null=True)
    shoesid = PrimaryKeyField(db_column='shoesID', null=True)

    class Meta:
        db_table = 'shoes'


class SqliteSequence(BaseModel):
    name = UnknownField(null=True)  # 
    seq = UnknownField(null=True)  # 

    class Meta:
        db_table = 'sqlite_sequence'


class Stepdata(BaseModel):
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    steps = IntegerField(null=True)
    stepspm = IntegerField(db_column='stepsPM', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'stepData'
        primary_key = CompositeKey('runid', 'sequenceid')


class Stepstopdetection(BaseModel):
    action = IntegerField(null=True)
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'stepStopDetection'
        primary_key = CompositeKey('runid', 'sequenceid')


class Stopdetection(BaseModel):
    action = IntegerField(null=True)
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'stopDetection'
        primary_key = CompositeKey('runid', 'sequenceid')


class Stopwatchstatusicon(BaseModel):
    enabled = BooleanField(null=True)
    iconid = IntegerField(db_column='iconID', null=True)
    iconindex = PrimaryKeyField(db_column='iconIndex', null=True)

    class Meta:
        db_table = 'stopwatchStatusIcon'


class Strava(BaseModel):
    accesstoken = TextField(db_column='accessToken', null=True)
    doneupload = IntegerField(db_column='doneUpload', null=True)
    key = PrimaryKeyField(null=True)
    stravaenabled = BooleanField(db_column='stravaEnabled', null=True)
    tokenresponsejson = TextField(db_column='tokenResponseJson', null=True)
    uploadformat = IntegerField(db_column='uploadFormat', null=True)
    username = TextField(null=True)

    class Meta:
        db_table = 'strava'


class Support(BaseModel):
    debugmode = BooleanField(db_column='debugMode', null=True)
    demo = BooleanField(null=True)
    demorunid = IntegerField(db_column='demoRunID', null=True)
    demotimeratio = UnknownField(db_column='demoTimeRatio', null=True)  # DOUBLE
    fauxlocation = BooleanField(db_column='fauxLocation', null=True)
    fauxlocationrunid = IntegerField(db_column='fauxLocationRunID', null=True)
    fauxmotion = BooleanField(db_column='fauxMotion', null=True)
    fauxmotionrunid = IntegerField(db_column='fauxMotionRunID', null=True)
    fauxlocationtimeratio = UnknownField(db_column='fauxlocationTimeRatio', null=True)  # DOUBLE
    key = PrimaryKeyField(null=True)
    locationrecords = BooleanField(db_column='locationRecords', null=True)
    motionrecords = BooleanField(db_column='motionRecords', null=True)
    networktrace = BooleanField(db_column='networkTrace', null=True)
    showrunid = BooleanField(db_column='showRunID', null=True)
    speakdisabled = BooleanField(db_column='speakDisabled', null=True)
    storedisabled = BooleanField(db_column='storeDisabled', null=True)
    usebikespeedcadencedata = BooleanField(db_column='useBikeSpeedCadenceData', null=True)
    useheartratedata = BooleanField(db_column='useHeartRateData', null=True)
    usestridedata = BooleanField(db_column='useStrideData', null=True)

    class Meta:
        db_table = 'support'


class Temperaturedata(BaseModel):
    runid = IntegerField(db_column='runID', null=True)
    sequenceid = IntegerField(db_column='sequenceID', null=True)
    temperature = UnknownField(null=True)  # DOUBLE
    timeoffset = UnknownField(db_column='timeOffset', null=True)  # DOUBLE

    class Meta:
        db_table = 'temperatureData'
        primary_key = CompositeKey('runid', 'sequenceid')


class Twitter(BaseModel):
    accesstoken = TextField(db_column='accessToken', null=True)
    accesstokensecret = TextField(db_column='accessTokenSecret', null=True)
    announceallowme = BooleanField(db_column='announceAllowMe', null=True)
    key = PrimaryKeyField(null=True)
    promptondone = BooleanField(db_column='promptOnDone', null=True)
    requesttoken = TextField(db_column='requestToken', null=True)
    requesttokensecret = TextField(db_column='requestTokenSecret', null=True)
    screenname = TextField(db_column='screenName', null=True)
    tweetatdistanceinterval = IntegerField(db_column='tweetAtDistanceInterval', null=True)
    tweetatdistanceintervalitems = TextField(db_column='tweetAtDistanceIntervalItems', null=True)
    tweetattimeinterval = IntegerField(db_column='tweetAtTimeInterval', null=True)
    tweetattimeintervalitems = TextField(db_column='tweetAtTimeIntervalItems', null=True)
    tweetendinterval = BooleanField(db_column='tweetEndInterval', null=True)
    tweetendintervalitems = TextField(db_column='tweetEndIntervalItems', null=True)
    tweetendsplit = BooleanField(db_column='tweetEndSplit', null=True)
    tweetendsplititems = TextField(db_column='tweetEndSplitItems', null=True)
    tweetoncontinue = BooleanField(db_column='tweetOnContinue', null=True)
    tweetoncontinueitems = TextField(db_column='tweetOnContinueItems', null=True)
    tweetondone = BooleanField(db_column='tweetOnDone', null=True)
    tweetondoneitems = TextField(db_column='tweetOnDoneItems', null=True)
    tweetonstart = BooleanField(db_column='tweetOnStart', null=True)
    tweetonstartitems = TextField(db_column='tweetOnStartItems', null=True)
    tweetonstop = BooleanField(db_column='tweetOnStop', null=True)
    tweetonstopitems = TextField(db_column='tweetOnStopItems', null=True)
    twitterannouncementstype = IntegerField(db_column='twitterAnnouncementsType', null=True)
    twitterenabled = BooleanField(db_column='twitterEnabled', null=True)
    userid = TextField(db_column='userID', null=True)
    userwhitelist = TextField(db_column='userWhiteList', null=True)

    class Meta:
        db_table = 'twitter'


class Voice(BaseModel):
    descriptiondict = TextField(db_column='descriptionDict', null=True)
    free = BooleanField(null=True)
    namedict = TextField(db_column='nameDict', null=True)
    productidsuffix = TextField(db_column='productIDSuffix', null=True, primary_key=True)
    voicefilename = TextField(db_column='voiceFileName', null=True)
    voiceid = TextField(db_column='voiceID', null=True)
    voicelocale = TextField(db_column='voiceLocale', null=True)
    voicesamplefilename = TextField(db_column='voiceSampleFileName', null=True)

    class Meta:
        db_table = 'voice'

