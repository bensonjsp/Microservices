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

type Hotel struct {
	HotelID       int    `json:"hotel_id"`
	HotelName     string `json:"hotel_name"`
	HotelLocation string `json:"hotel_location"`
}

func main() {
	initDB()

	router := gin.Default()
	router.GET("/gethotel", getHotels)

	router.Run("0.0.0.0:5001")
}

func initDB() {
	dbURL := os.Getenv("HOTEL_DB_URL")
	// Capture connection properties.
	cfg := mysql.Config{
		User:                 "admin",
		Passwd:               "admin",
		Net:                  "tcp",
		Addr:                 dbURL,
		DBName:               "hotel_db",
		AllowNativePasswords: true,
	}
	// Get a database handle.
	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}
}

// Query database for hotels
func allHotels() []Hotel {
	rows, err := db.Query("SELECT * FROM hotel")
	if err != nil {
		fmt.Println("Error in Query")
	}
	defer rows.Close() // save resources

	hotels := []Hotel{}
	for rows.Next() {
		var h Hotel
		if err := rows.Scan(&h.HotelID, &h.HotelName, &h.HotelLocation); err != nil {
			fmt.Println("Error in retrieving row")
		}
		hotels = append(hotels, h)
	}
	fmt.Printf("Hotels found: %v\n", hotels)
	return hotels
}

// getHotels responds with the list of all hotels as JSON i.e. Convert to JSON
func getHotels(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"code": 200,
		"data": gin.H{"hotels": allHotels()},
	})
}
