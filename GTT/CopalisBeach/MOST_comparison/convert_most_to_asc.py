
import most_tools

fname_most = 'Copalia_Agrid_15s_etopo2022.most'
Agrid = most_tools.read_most_grid(fname_most)
fname_asc = fname_most.replace('.most','.asc')
Agrid.write(fname_asc, topo_type=3, header_style='asc', Z_format='%.3f')
print('Created ',fname_asc)

fname_most = 'Copalis_Bgrid_3sec_mhw_13DEM_CUDEM_combine.most'
Bgrid = most_tools.read_most_grid(fname_most)
fname_asc = fname_most.replace('.most','.asc')
Bgrid.write(fname_asc, topo_type=3, header_style='asc', Z_format='%.3f')
print('Created ',fname_asc)

fname_most = 'copalis_Cgrid_10m_mhw.most'
Cgrid = most_tools.read_most_grid(fname_most)
fname_asc = fname_most.replace('.most','.asc')
Cgrid.write(fname_asc, topo_type=3, header_style='asc', Z_format='%.3f')
print('Created ',fname_asc)

