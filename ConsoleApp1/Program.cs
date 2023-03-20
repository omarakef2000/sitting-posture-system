using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        string host = "127.0.0.1";
        int port = 5000;
        IPAddress ip = IPAddress.Parse(host);
        IPEndPoint remoteEP = new IPEndPoint(ip, port);

        Socket sender = new Socket(ip.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        try
        {
           
            sender.Connect(remoteEP);
            Console.WriteLine($"Connected to {sender.RemoteEndPoint}");
            string message = "Robin’s iphone";
            byte[] data = Encoding.ASCII.GetBytes(message);
            int bytesSent = sender.Send(data);
            Console.WriteLine($"Sent {bytesSent} bytes");
            byte[] buffer = new byte[1024];
            int bytesReceived = sender.Receive(buffer);
            string response = Encoding.ASCII.GetString(buffer, 0, bytesReceived);
            Console.WriteLine($"Received: {response}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Exception: {e.ToString()}");
        }
        finally
        {
            sender.Shutdown(SocketShutdown.Both);
            sender.Close();
        }
    }
}
