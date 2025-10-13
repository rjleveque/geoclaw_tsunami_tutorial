"""
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.

"""
import sys
import os
import numpy as np

# if some values in .data files show up as e.g. np.float64(3600.0)
# this will restore old behavior and just print 3600.0:
#np.set_printoptions(legacy="1.25")
# fixed in clawpack versions >= v5.13.0

from clawpack.amrclaw.data import FlagRegion

try:
    CLAW = os.environ['CLAW']
except:
    raise Exception("*** Must first set CLAW enviornment variable")


try:
    root_dir = os.environ['GTT']
except:
    raise Exception("*** Must first set GTT enviornment variable")
    raise Exception("*** Perhaps to point to geoclaw_tsunami_tutorial/GTT")

topodir =  root_dir + '/topo/topofiles'
dtopodir = root_dir + '/dtopo/dtopofiles'


#------------------------------
def setrun(claw_pkg='geoclaw'):
#------------------------------

    """
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "geoclaw" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData

    """

    from clawpack.clawutil import data

    assert claw_pkg.lower() == 'geoclaw',  "Expected claw_pkg = 'geoclaw'"

    num_dim = 2
    rundata = data.ClawRunData(claw_pkg, num_dim)


    #------------------------------------------------------------------
    # Problem-specific parameters to be written to setprob.data:
    #------------------------------------------------------------------
    #probdata = rundata.new_UserData(name='probdata',fname='setprob.data')

    #------------------------------------------------------------------
    # Standard Clawpack parameters to be written to claw.data, amr.data:
    #------------------------------------------------------------------
    clawdata = rundata.clawdata  # initialized when rundata instantiated

    # Set single grid parameters first.
    # See below for AMR parameters.

    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.num_dim = num_dim      # should always be 2 in GeoClaw

    # Lower and upper edge of computational domain:

    clawdata.lower[0] = -128.5      # west longitude
    clawdata.upper[0] = -123.5      # east longitude

    clawdata.lower[1] = 45.         # south latitude
    clawdata.upper[1] = 49.         # north latitude

    # Number of grid cells: Coarsest grid is 4 arcminutes (1/15 degree)
    clawdata.num_cells[0] =  5*15
    clawdata.num_cells[1] =  4*15

    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.num_eqn = 3

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.num_aux = 3

    # Index of aux array corresponding to capacity function, if there is one:
    clawdata.capa_index = 2

    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.  # Start time in seconds

    # Restart from checkpoint file of a previous run?
    # If restarting, t0 above should be from original run, and the
    # restart_file 'fort.chkNNNNN' specified below should be in
    # the OUTDIR indicated in Makefile.

    clawdata.restart = False     # True to restart from prior results
    clawdata.restart_file = ''   # File to use for restart data

    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.

    clawdata.output_style = 1

    if clawdata.output_style==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.num_output_times = 9
        clawdata.tfinal = 1.5*3600.
        clawdata.output_t0 = True  # output at initial (or restart) time?

    elif clawdata.output_style == 2:
        # Specify a list of output times.
        # e.g. at 0 and 60 seconds and then less frequently:
        clawdata.output_times = [0.,60., 1800., 3600., 5400.]

    elif clawdata.output_style == 3:
        # Output every iout timesteps with a total of ntot time steps:
        clawdata.output_step_interval = 1
        clawdata.total_steps = 3
        clawdata.output_t0 = True


    clawdata.output_format = 'binary32'      # 'ascii', 'binary', or 'binary32'
    clawdata.output_q_components = 'all'     # output all 3 components h,hu,hv


    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 3

    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = True

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 0.2

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used
    clawdata.cfl_desired = 0.85
    # max Courant number to allow without retaking step with a smaller dt:
    clawdata.cfl_max = 1.0

    # Maximum number of time steps to allow between output times:
    clawdata.steps_max = 5000

    # ------------------
    # Method to be used:
    # ------------------

    # Order of accuracy:  1 => Godunov,  2 => Lax-Wendroff plus limiters
    clawdata.order = 2

    # Use dimensional splitting? (not yet available for AMR)
    clawdata.dimensional_split = 'unsplit'

    # For unsplit method, transverse_waves can be
    #  0 or 'none'      ==> donor cell (only normal solver used)
    #  1 or 'increment' ==> corner transport of waves
    #  2 or 'all'       ==> corner transport of 2nd order corrections too
    clawdata.transverse_waves = 2

    # Number of waves in the Riemann solution:
    clawdata.num_waves = 3

    # List of limiters to use for each wave family:
    # Required:  len(limiter) == num_waves
    # Some options:
    #   0 or 'none'     ==> no limiter (Lax-Wendroff)
    #   1 or 'minmod'   ==> minmod
    #   2 or 'superbee' ==> superbee
    #   3 or 'mc'       ==> MC limiter
    #   4 or 'vanleer'  ==> van Leer
    clawdata.limiter = ['mc', 'mc', 'mc']

    clawdata.use_fwaves = True    # True ==> use f-wave version of algorithms

    # Source terms splitting:
    #   src_split == 0 or 'none'    ==> no source term (src routine never called)
    #   src_split == 1 or 'godunov' ==> Godunov (1st order) splitting used,
    #   src_split == 2 or 'strang'  ==> Strang (2nd order) splitting used,  not recommended.
    clawdata.source_split = 1

    # --------------------
    # Boundary conditions:
    # --------------------

    # Number of ghost cells (usually 2)
    clawdata.num_ghost = 2

    # Choice of BCs at xlower and xupper:
    #   0 => user specified (must modify bcN.f to use this option)
    #   1 => extrapolation (non-reflecting outflow)
    #   2 => periodic (must specify this at both boundaries)
    #   3 => solid wall for systems where q(2) is normal velocity

    clawdata.bc_lower[0] = 'extrap'
    clawdata.bc_upper[0] = 'extrap'

    clawdata.bc_lower[1] = 'extrap'
    clawdata.bc_upper[1] = 'extrap'

    # --------------
    # Checkpointing:
    # --------------

    # Specify when checkpoint files should be created that can be
    # used to restart a computation.

    # negative checkpoint_style means alternate between aaaaa and bbbbb files
    # so that at most 2 checkpoint files exist at any time, useful when
    # doing frequent checkpoints of large problems.

    clawdata.checkpt_style = 0

    if clawdata.checkpt_style == 0:
        # Do not checkpoint at all
        pass

    elif clawdata.checkpt_style == 1:
        # Checkpoint only at tfinal.
        pass

    elif abs(clawdata.checkpt_style) == 2:
        # Specify a list of checkpoint times.
        clawdata.checkpt_times = 1800.*np.arange(1,6,1)

    elif abs(clawdata.checkpt_style) == 3:
        # Checkpoint every checkpt_interval timesteps (on Level 1)
        # and at the final time.
        clawdata.checkpt_interval = 5

    # ---------------
    # AMR parameters:
    # ---------------
    amrdata = rundata.amrdata

    # maximum size of each grid patch (in each direction):
    amrdata.max1d = 60    # default is 60

    # initial size of work array for AMR patches:
    amrdata.memsize = 10000000   # default is 1000000

    # max number of refinement levels:
    amrdata.amr_levels_max = 3

    # List of refinement ratios at each level (length at least mxnest-1)

    # Set up for 8 levels here, possibly using fewer:
    # dx = dy = 4', 2', 24", 12", 6", 3", 1", 1/3"
    refinement_ratios = [2,5,2,2,2,3,3]
    amrdata.refinement_ratios_x = refinement_ratios
    amrdata.refinement_ratios_y = refinement_ratios
    amrdata.refinement_ratios_t = refinement_ratios

    # Specify type of each aux variable in amrdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    amrdata.aux_type = ['center','capacity','yleft']

    # Flag using refinement routine flag2refine rather than richardson error
    amrdata.flag_richardson = False    # use Richardson?
    amrdata.flag2refine = True

    # steps to take on each level L between regriddings of level L+1:
    amrdata.regrid_interval = 3

    # width of buffer zone around flagged points:
    # (typically the same as regrid_interval so waves don't escape):
    amrdata.regrid_buffer_width  = 2

    # clustering alg. cutoff for (# flagged pts) / (total # of cells refined)
    # (closer to 1.0 => more small grids may be needed to cover flagged cells)
    amrdata.clustering_cutoff = 0.7

    # print info about each regridding up to this level:
    amrdata.verbosity_regrid = 3

    # ------------------------------
    # Set data specific to GeoClaw:
    # ------------------------------

    # Refinement settings
    refinement_data = rundata.refinement_data
    refinement_data.variable_dt_refinement_ratios = True
    refinement_data.wave_tolerance = 0.1


    geo_data = rundata.geo_data

    # == Physics ==
    geo_data.gravity = 9.81
    geo_data.coordinate_system = 2
    geo_data.earth_radius = 6367.5e3

    # == Forcing Options
    geo_data.coriolis_forcing = False

    # == Algorithm and Initial Conditions ==
    geo_data.sea_level = 0.0
    geo_data.dry_tolerance = 1.e-3
    geo_data.friction_forcing = True
    geo_data.manning_coefficient =.025
    geo_data.friction_depth = 200
    geo_data.speed_limit = 20.  # limit on speed sqrt(u**2 + v**2)

    # ---------------
    # TOPO:
    # ---------------
    # == topo.data values ==
    topo_data = rundata.topo_data

    topofiles = topo_data.topofiles   # empty list initially
    # for topography, append tuples/lists of the form:
    #    [topotype, fname]

    # 30-sec topo:
    topo_file = os.path.join(topodir, 'etopo22_30s_-130_-122_40_50_30sec.asc')
    topofiles.append([3, topo_file])

    # 1/3 arcsec topo
    topo_file = os.path.join(topodir, 'Copalis_13s.asc')
    topofiles.append([3, topo_file])


    # ---------------
    # DTOPO:
    # ---------------
    # == setdtopo.data values ==
    dtopo_data = rundata.dtopo_data
    dtopofile = os.path.join(dtopodir, 'ASCE_SIFT_Region2.dtt3')
    dtopo_data.dtopofiles = [[3, dtopofile]]
    dtopo_data.dt_max_dtopo = 0.2  # max timestep (sec) while topo is changing


    # ---------------
    # qinit:
    # ---------------
    # == setqinit.data values ==
    rundata.qinit_data.qinit_type = 0
    rundata.qinit_data.qinitfiles = []
    # for qinit perturbations, append lines of the form: (<= 1 allowed for now!)
    #   [minlev, maxlev, fname]
    rundata.qinit_data.variable_eta_init = True  # for subsidence/uplift


    # ---------------
    # Force dry:
    # ---------------
    if 0:
        # None for this project
        name = 'force_dry_init.data'
        force_dry_fname = os.path.join(input_dir, name)
        force_dry = ForceDry()
        force_dry.tend = 1e9
        force_dry.fname = force_dry_fname
        rundata.qinit_data.force_dry_list.append(force_dry)


    # ---------------
    # REGIONS:
    # ---------------

    flagregions = rundata.flagregiondata.flagregions  # empty list initially

    # Computational domain Variable Region:
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_domain'
    flagregion.minlevel = 1
    flagregion.maxlevel = 2
    flagregion.t1 = 0.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    x1,y1 = clawdata.lower
    x2,y2 = clawdata.upper
    # Domain is [x1,x2,y1,y2], and add a buffer around it (not really needed):
    flagregion.spatial_region = [x1-0.2, x2+0.2, y1-0.2, y2+0.2]
    flagregions.append(flagregion)

    # dtopo region - force refinement even before there is any deformation
    # to the resolution needed to resolve the initial waves well.
    # This region forces a certain level of refinement over a short time.
    # Normally this would cover all of dtopo, but for this simplified
    # test problem the domain is truncated and we are only going out to
    # a short time so we don't need to refine even all of the dtopo within
    # the domain.
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_dtopo'
    flagregion.minlevel = 4
    flagregion.maxlevel = 4
    flagregion.t1 = 0.
    flagregion.t2 = 10.
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-126.6,-124.,45.5,48.5]
    flagregions.append(flagregion)


    # Region12sec - 24 to  12 sec:
    # This allows 4 levels, starting after the dtopo deformation ends
    # (other regions below will force/allow more refinement)
    flagregion = FlagRegion(num_dim=2)
    flagregion.name = 'Region_12sec'
    flagregion.minlevel = 3
    flagregion.maxlevel = 4
    flagregion.t1 = 10.
    flagregion.t2 = 1e9
    flagregion.spatial_region_type = 1  # Rectangle
    flagregion.spatial_region = [-126.6,-124.,46.27,47.68]
    flagregions.append(flagregion)


    # ---------------
    # GAUGES:
    # ---------------

    gauges = rundata.gaugedata.gauges   # empty list initially
    # for gauges append tuples/lists of the form
    #   [gaugeno, x, y, t1, t2]

    gauges.append([101, -124.1899537, 47.1159722, 0, 1e9])     # slightly offshore
    gauges.append([102, -124.1800463, 47.1159722, 0, 1e9])     # onshore
    gauges.append([103, -124.1706019, 47.1159722, 0, 1e9])     # in river

    rundata.gaugedata.file_format = 'ascii'  # often use 'binary32'
    #rundata.gaugedata.min_time_increment = 5 # minimum seconds between outputs


    # -----------------------------
    # FGMAX GRIDS:
    # ------------------------------
    # set num_fgmax_val = 1 to save only max depth,
    #                     2 to also save max speed,
    #                     5 to also save max hs,hss,hmin
    rundata.fgmax_data.num_fgmax_val = 2
    fgmax_grids = rundata.fgmax_data.fgmax_grids  # empty list initially


    # -----------------------------
    # FGOUT GRIDS:
    # ------------------------------

    fgout_grids = rundata.fgout_data.fgout_grids  # empty list initially

    # ---------------
    # FOR DEVELOPERS:
    # ---------------

    # Toggle debugging print statements:
    amrdata.dprint = False      # print domain flags
    amrdata.eprint = False      # print err est flags
    amrdata.edebug = False      # even more err est flags
    amrdata.gprint = False      # grid bisection/clustering
    amrdata.nprint = False      # proper nesting output
    amrdata.pprint = False      # proj. of tagged points
    amrdata.rprint = False      # print regridding summary
    amrdata.sprint = False      # space/memory output
    amrdata.tprint = False       # time step reporting each level
    amrdata.uprint = False      # update/upbnd reporting

    return rundata

if __name__ == '__main__':

    # Set up run-time parameters and write all data files.
    import sys
    rundata = setrun(*sys.argv[1:])
    rundata.write()

    # To create kml files of inputs:
    from clawpack.geoclaw import kmltools
    kmltools.make_input_data_kmls(rundata)
