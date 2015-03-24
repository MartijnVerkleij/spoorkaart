<?php
	require 'station.php';
	require 'track.php' ;
	
	$instance = new DutchRailwayGraph();
	
	echo 'bla';

	class DutchRailwayGraph
	{
		public $stations;
		public $tracks;
		
		public function __construct() {
			
			include 'data/raildata.php';
			
			foreach ($stationdata as $station) {
				$this->addStation($station[0], $station[1]);
			}
			
			foreach ($trackdata as $track) {
				$this->addTrack($track[0], $track[1]);
			}
		}
		
		public function addStation($acr, $name) {
			$this->$stations[$acr] = new station($acr, $name);
		}
		public function addTrack($station1, $station2) {
			$this->$tracks[] = new track($station1, $station2);
		}

		public function getType($station) {
			switch ($this->edgeCount($station)) {
				case 1: return "end"; break;
				case 2: return "normal"; break;
				default: return "transit"; break;
			}
		}
		
		private function edgeCount($station) {
			$i = 0;
			foreach ($tracks as $track) {
				if ($track->station1 == $station || $track->station2 == $station) {
					$i++;
				}
			}
			return $i;
		}
		
		
	}

?>
