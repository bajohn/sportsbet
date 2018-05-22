results found on: https://swishanalytics.com/optimus/mlb/mlb-daily-fantasy-lineup-results
PAST data from: https://www.mysportsfeeds.com/data-feeds/subscriptions

MLB pitch fx data sample: http://gd2.mlb.com/components/game/mlb/year_2017/month_04/day_05/gid_2017_04_05_nyamlb_tbamlb_1/inning/inning_4.xml

Steps:
1. parse XML data to JSON
2. for each hitter, find performance vs each type of pitch statistic
3. will need an efficient way to parse through all pitch data, but for major hitters, one season per hitter may be enough.
4. machine learning: after data is organized, train a neural net for each hitter. Features are input pitch statistics, like velocity, movement, etc etc
5. really, want the outcome of each at bat, so should train over an at bat.
6. "labels", the outcomes to train against, are the results of each at bat
7. Therefore a single "labeled example" would look like:

    -pitch1 speed
    -pitch1 movement
    -pitch1 other stats
    ...
    -pitch2 speed 
    -pitch2 movement
    -pitch2 other stats
    ...
    --->neural net---->
    outcome = base hit

8. other consideration: should make a database to store all this player data. Probably SQL; what is easiest way? Probably sqlalchemy with mysql. figure out best way to run this locally.
9. one option: mysql workbench already appears working, on localhost:3306. java code from javatwitter that was working:
        data_source.setUrl("jdbc:mysql://localhost:3306/javatwitter?useSSL=false");
        data_source.setUsername("root");
        data_source.setPassword("thisguy");

10. db structure?

player table:
    player name
    player id
    ?

at bat table:
    at bat id
    player id
    pitcher id
    (R/L:)
    p_throws 
    start speed
    end speed
    (initial point:)
    x0
    y0 
    z0 
    (end point:)
    px 
    py 
    pz
    (break amount:)
    pfx_x 
    pfx_y 
    pfx_z
    (velocity:)
    vx0
    vy0
    vz0
    (acceleration:)
    ax
    ay 
    az
    (break stats:)
    break_y
    break_angle
    break_length
    spin_rate
    spin_dir


Stats can prob ignore:
    x, y, z (not sure what these are)
    nasty factor (derivative)
    zone (deriivative)




player tables
pitch1 table? 

think about neural net: it will need to take in each pitch's data from the single at bat, then map to an outcome. multi-label classification task? see the following for keras implementation:
https://www.depends-on-the-definition.com/guide-to-multi-label-classification-with-neural-networks/

Will feed pitcher avg pitch stats into neural net for outcome