import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship, Session
from sqlalchemy import create_engine
 


# todo- backref for optimization. prob not that important for this application.

class DB():

    def __init__(self):
        metadata = MetaData()



        pitch = Table('pitch', metadata,
        Column('play_guid', String(250), primary_key=True), #identifies at bat
        Column('p_throws', String(250), nullable=False),
        Column('des', String(250), nullable=True),
        Column('des_es', String(250), nullable=False),
        Column('id', String(250), nullable=False), # probably ignore this
     
        Column('type', String(250), nullable=False),
        Column('code', String(250), nullable=False),
        Column('tfs', String(250), nullable=False),
        Column('tfs_zulu', String(250), nullable=False),
        Column('x', Float, nullable=False),
        Column('y', Float, nullable=False),
        Column('event_num', Float, nullable=False),
        Column('sv_id', String(250), nullable=False),
        Column('start_speed', Float, nullable=False),
        Column('end_speed', Float, nullable=False),
        Column('sz_top', Float, nullable=False),
        Column('sz_bot', Float, nullable=False),
        Column('pfx_x', Float, nullable=False),
        Column('pfx_z', Float, nullable=False),
        Column('px', Float, nullable=False),
        Column('pz', Float, nullable=False),
        
        Column('x0', Float, nullable=False),
        Column('y0', Float, nullable=False),
        Column('z0', Float, nullable=False),
        Column('vx0', Float, nullable=False),
        Column('vy0', Float, nullable=False),
        Column('vz0', Float, nullable=False),
        
        Column('ax', Float, nullable=False),
        Column('ay', Float, nullable=False),
        Column('az', Float, nullable=False),

        Column('break_y', Float, nullable=False),
        Column('break_angle', Float, nullable=False),
        Column('break_length', Float, nullable=False),
        Column('pitch_type', String(250), nullable=False),
        Column('type_confidence', Float, nullable=False),
        Column('zone', Float, nullable=False),
        Column('nasty', Float, nullable=False),
        Column('spin_dir', Float, nullable=False),
        Column('spin_rate', Float, nullable=False),
        Column('cc', String(250), nullable=False),
        Column('mt', String(250), nullable=False),

        )

        
        pitchAvg = Table('pitchAvg', metadata,
        Column('play_guid', String(250), primary_key=True), #identifies at bat
        Column('p_throws', String(250), nullable=False),
        Column('des', String(250), nullable=True),
        Column('des_es', String(250), nullable=False),
        Column('id', String(250), nullable=False), # probably ignore this
     
        Column('type', String(250), nullable=False),
        Column('code', String(250), nullable=False),
        Column('tfs', String(250), nullable=False),
        Column('tfs_zulu', String(250), nullable=False),
        Column('x', Float, nullable=False),
        Column('y', Float, nullable=False),
        Column('event_num', Float, nullable=False),
        Column('sv_id', String(250), nullable=False),
        Column('start_speed', Float, nullable=False),
        Column('end_speed', Float, nullable=False),
        Column('sz_top', Float, nullable=False),
        Column('sz_bot', Float, nullable=False),
        Column('pfx_x', Float, nullable=False),
        Column('pfx_z', Float, nullable=False),
        Column('px', Float, nullable=False),
        Column('pz', Float, nullable=False),
        
        Column('x0', Float, nullable=False),
        Column('y0', Float, nullable=False),
        Column('z0', Float, nullable=False),
        Column('vx0', Float, nullable=False),
        Column('vy0', Float, nullable=False),
        Column('vz0', Float, nullable=False),
        
        Column('ax', Float, nullable=False),
        Column('ay', Float, nullable=False),
        Column('az', Float, nullable=False),

        Column('break_y', Float, nullable=False),
        Column('break_angle', Float, nullable=False),
        Column('break_length', Float, nullable=False),
        Column('pitch_type', String(250), nullable=False),
        Column('type_confidence', Float, nullable=False),
        Column('zone', Float, nullable=False),
        Column('nasty', Float, nullable=False),
        Column('spin_dir', Float, nullable=False),
        Column('spin_rate', Float, nullable=False),
        Column('cc', String(250), nullable=False),
        Column('mt', String(250), nullable=False),

        )
        # pitchStatList =['des', 'des_es', 'id', 'type', 'tfs', 'tfs_zulu', 'x', 'y', 'event_num', 'sv_id', 'play_guid', 'start_speed', 'end_speed', 'sz_top', 'sz_bot', 'pfx_x', 'pfx_z', 'px', 'pz', 'x0', 'y0', 'z0', 'vx0', 'vy0', 'vz0', 'ax', 'ay', 'az', 'break_y', 'break_angle', 'break_length', 'pitch_type', 'type_confidence', 'zone', 'nasty', 'spin_dir', 'spin_rate', 'cc', 'mt']

        matchup = Table('matchup', metadata,
        Column('id', String(250), primary_key=True),
        Column('batter_id', None,  ForeignKey('batter.id')),
        Column('pitcher_id', None, ForeignKey('pitcher.id')),
        Column('outcome', String(250), nullable=False),
        Column('outcomeVal', Integer, nullable=False)
        )

        batter = Table('batter', metadata,
        Column('id', Integer, primary_key=True),
        Column('batter_name', String(250), nullable=False)
        )

        pitcher = Table('pitcher', metadata,
        Column('id', Integer, primary_key=True),
        Column('pitcher_name', String(250), nullable=False))
        # Column('tendency_id', None, ForeignKey('tendency.id'), nullable=False ))

        # probably won't need this tendency table early on, most of this can be done in memory.
        tendency = Table('tendency', metadata,
        Column('id', Integer, primary_key=True),
        Column('pitcher_id', None, ForeignKey('pitcher.id')),
        Column('num_thrown', Integer, nullable=False),
        Column('pitch_type',  String(250), nullable=False))
        
        Base = automap_base()
        engine = create_engine('mysql+mysqldb://root:thisguy@localhost/sportsbet')

        metadata.create_all(engine)


        Base.prepare(engine, reflect=True)
        self.Batter = Base.classes.batter
        self.Pitcher = Base.classes.pitcher
        self.Pitch = Base.classes.pitch
        self.Matchup = Base.classes.matchup
        self.Tendency = Base.classes.tendency

        self.session = Session(engine)


