# inspired from 
# https://github.com/israel-dryer/Raspberry-Pi-Sensors/blob/master/ds18b20_single.py

# to mount the device
system('modprobe w1-gpio') 
system('modprobe w1-therm')
puts "mount ok"

# get the file that contains the data:
base_dir = '/sys/bus/w1/devices'
# puts base_dir
device_path = Dir.glob(File.join(base_dir, '28*')) # 28 is the prefix -> ds18b20
# puts device_path
@device_file = "#{device_path[0]}/w1_slave" # the file that gathers the data
puts @device_file

def read_raw_data()
    file = File.open(@device_file)
    file_data = file.readlines.map(&:chomp)
    # puts file_data
end

def get_temp()
    validity, raw_data = read_raw_data

    # wait for a valid measure
    while !validity.include?("YES")
        sleep (1)
        validity, raw_data = read_raw_data
    end

    data_idx = raw_data.index("t=")
    if data_idx != -1
        puts raw_data
        data_str = raw_data[data_idx + 2..-1]
        data = data_str.to_f/1000.0
        puts "#{data}°C"
    end


end

puts "start"
# puts device_file
get_temp
    
