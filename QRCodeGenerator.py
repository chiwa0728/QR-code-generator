import qrcode
import os

# Folder to save QR Pictures ((CHANGE PATH FOLDER TO TRY))
save_folder = r"C:\Users\Sample\Documents"

# Create folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

while True:
    # Ask for URL
    url = input("\nEnter the URL: ").strip()

    # Ask for file name
    file_name = input("Enter file name: ").strip()

    # Combine folder + filename
    file_path = os.path.join(save_folder, f"{file_name}.png")

    # Generate QR code
    img = qrcode.make(url)

    # Save QR code
    img.save(file_path)

    # Output confirmation
    print("\nGenerated successfully!")
    print("Saved at:")
    print(file_path)

    # Ask if user wants another QR code
    again = input("\nGenerate another QR code? (yes/no): ").strip().lower()

    if again != "yes":
        print("\nThank you for using QR Generator!")
        break