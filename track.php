<?php
	class track {
		public $station1;
		public $station2;
		public $width = 1;
		
		public function __construct($stationArg1, $stationArg2) {
			$this->station1 = $stationArg1;
			$this->station2 = $stationArg2;
		}
	}
?>