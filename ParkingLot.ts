
interface ParkingSpot {
  vehicle: string | null
  type: "compact" | "regular" | "motorcycle" | "large";
  available: Boolean
}

interface VanParkingSpot extends ParkingSpot {
  vehicle: "van"
  type: "regular" | "large";
  available: false
}

interface CarParkingSpot extends ParkingSpot {
  vehicle: "car" 
  type: "compact"  | "regular";
  available: false
}


class ParkingLot {
  spots: Array<ParkingSpot> = [];
  constructor(spots: Array<ParkingSpot>) {
    this.spots = spots;
    //  Throw error if total regular spots taken by vans !% 3
    if (this.numSpotsTakenByVans("regular") % 3 !== 0)
      throw new Error("Vans must take 3 regular parking spots!")
  }
  /**
   * @return the amount of spots left
   */
  spotsLeft(type:string = "") {
      let spotsLeft = 0
      this.spots.forEach((spot: ParkingSpot) => {
        // If there is a type given
        if (type){
          if (spot.available && type === spot.type){
            spotsLeft ++;
          }
        } else {
          spotsLeft ++;
        }
      })
      return spotsLeft;
  }

  /**
   * @return the total number of spots
   */
  totalSpots() {
    return this.spots.length
  }

  /**
   * @return true if parking lot is full else false
   */
  isFull(){
    if (this.spotsLeft() === 0) return true
    else return false; 
  }

  /**
   * @return true if parking lot is empty else false
   */
  isEmpty(){
    // A parking lot is only empty if it has total number of spots available
    if (this.spotsLeft() === this.totalSpots()) return true
    else return false; 
  }

  /**
   * @param type is the certain ParkingSpot type we are checking is full
   * @returns true if full else false
   */
  isParkingTypeFull(type: string){
    // A parking type will only be full when the spots left for those  types = 0
    if (this.spotsLeft(type) === 0) return true
    else return false;
  }

  /**
   * @param type is an optional parameter to check specific parking spot taken up by vans
   * @returns the amount of spots vans are taking up
   */
  numSpotsTakenByVans(type: string = ""){
    // W
    let numOfSpots = 0 
    this.spots.forEach((spot: ParkingSpot) => {
      if (spot.vehicle === "van" && type){
        // We can assume uavailable parking spot
        if (spot.type === type){
          numOfSpots++;
        }
      } else if (spot.vehicle === "van") {
        numOfSpots ++;
      }

    })
    return numOfSpots
  }
}

let data: ParkingSpot[] = [
  {
    vehicle: null,
    type: "large", 
    available: true
  }, 
  {
    vehicle: null,
    type: "compact", 
    available: true
  }, 
  {
    vehicle: "van",
    type: "regular", 
    available: false
  }, 
  {
    vehicle: "car",
    type: "compact", 
    available: false
  }, 
  {
    vehicle: "van",
    type: "regular", 
    available: false
  },
  {
    vehicle: "van",
    type: "regular", 
    available: false
  },
  {
    vehicle: "van",
    type: "large", 
    available: false
  },
]

let parkingLot = new ParkingLot(data);
console.log(parkingLot.numSpotsTakenByVans())
