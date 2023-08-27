using System.Net.Sockets;
using System.Text;

﻿namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Это наш сервер");
            OurServer server = new OurServer();
        }
    }
}
