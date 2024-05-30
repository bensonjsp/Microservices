package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/go-sql-driver/mysql"
)

var db *sql.DB

type Room struct {
	RoomID      int    `json:"room_id"`
	HotelID     int    `json:"hotel_id"`
	HotelName   string `json:"hotel_name"`
	RoomNumber  int    `json:"room_number"`
	RoomSize    int    `json:"room_size"`
	RoomVacancy string `json:"room_vacancy"`
}

func main() {
	initDB()

	router := gin.Default()
	router.GET("/getroom", getRooms)

	router.Run("0.0.0.0:5002")
}

func initDB() {
	dbURL := os.Getenv("ROOM_DB_URL")
	// Capture connection properties.
	cfg := mysql.Config{
		User:                 "admin",
		Passwd:               "admin",
		Net:                  "tcp",
		Addr:                 dbURL,
		DBName:               "room_db",
		AllowNativePasswords: true,
	}
	// Get a database handle.
	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}
}

// Query database for rooms
func allRooms() []Room {
	rows, err := db.Query("SELECT * FROM room")
	if err != nil {
		fmt.Println("Error in Query")
	}
	defer rows.Close() // save resources

	rooms := []Room{}
	for rows.Next() {
		var r Room
		if err := rows.Scan(&r.RoomID, &r.HotelID, &r.HotelName, &r.RoomNumber, &r.RoomSize, &r.RoomVacancy); err != nil {
			fmt.Println("Error in retrieving row")
		}
		rooms = append(rooms, r)
	}
	fmt.Printf("Rooms found: %v\n", rooms)
	return rooms
}

// getRooms responds with the list of all rooms as JSON i.e. Convert to JSON
func getRooms(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"code": 200,
		"data": gin.H{"rooms": allRooms()},
	})
}
